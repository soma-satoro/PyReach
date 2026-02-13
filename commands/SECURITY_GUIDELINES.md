# Security Guidelines for PyReach Commands

## Overview

This document outlines security best practices and guidelines for developing commands in the PyReach system. Following these guidelines helps prevent security vulnerabilities and ensures consistent security practices across the codebase.

## ✅ **SECURITY FIXES IMPLEMENTED**

### 1. **Permission System Hardening**
- ✅ Fixed critical permission bypass in `base.py` StaffOnlyMixin
- ✅ Added centralized permission checking utilities
- ✅ Standardized permission checks in `CmdStaff.py`
- ✅ All admin commands now use consistent permission validation

### 2. **Input Validation & Sanitization**
- ✅ Added comprehensive input validation to `InputValidationMixin`
- ✅ Implemented length limits for all user inputs
- ✅ Added sanitization for control characters and injection attempts
- ✅ Enhanced clue creation with proper validation (`investigation.py`)
- ✅ Added character name validation in voting system

### 3. **Attribute Access Security**
- ✅ Implemented whitelist-based attribute access in `safe_getattr()`/`safe_setattr()`
- ✅ Added field validation for clue object modifications (`mystery_admin.py`)
- ✅ Protected against arbitrary attribute manipulation

### 4. **File Operation Security**
- ✅ Secured file operations in jobs system (`jobs_commands.py`)
- ✅ Added path traversal protection using `pathlib`
- ✅ Implemented proper exception handling for file operations
- ✅ Added directory validation to prevent unauthorized file access

## 🛡️ **SECURITY BEST PRACTICES**

### **1. Permission Checking**

**✅ CORRECT:**
```python
from commands.base import AdminOnlyMixin

class MyCommand(MuxCommand, AdminOnlyMixin):
    def func(self):
        if not self.check_admin_access():
            return
        # Admin-only code here
```

**❌ AVOID:**
```python
# Don't use inline permission checks
if self.caller.check_permstring("Admin"):
    # This is inconsistent and harder to maintain
```

### **2. Input Validation**

**✅ CORRECT:**
```python
from commands.base import BasePyReachCommand

class MyCommand(BaseExordiumCommand):  # BaseExordiumCommand = base game command class
    def func(self):
        # Use the built-in validation methods
        if not self.validate_input_length(self.args, self.MAX_MESSAGE_LENGTH, "Message"):
            return
        
        sanitized_input = self.sanitize_input(self.args)
        # Use sanitized_input for processing
```

**❌ AVOID:**
```python
# Don't trust user input directly
user_data = self.args  # Potentially dangerous
setattr(obj, user_controlled_attr, user_data)  # Very dangerous!
```

### **3. Attribute Access**

**✅ CORRECT:**
```python
# Use safe attribute access methods
value = self.safe_getattr(target, attribute_name, default_value)
success = self.safe_setattr(target, attribute_name, new_value)
```

**❌ AVOID:**
```python
# Don't use dynamic attribute access with user input
setattr(obj, user_input, value)  # Dangerous!
value = getattr(obj, user_controlled_name)  # Dangerous!
```

### **4. Command Argument Parsing**

**✅ CORRECT:**
```python
# Use the safe parsing method
parts = self.parse_equals_syntax(self.args, required_parts=2)
if not parts:
    self.caller.msg("Usage: command <arg1>=<arg2>")
    return

arg1, arg2 = parts
```

**❌ AVOID:**
```python
# Don't split without validation
parts = self.args.split("=")  # Could fail or return unexpected results
arg1, arg2 = parts  # Could crash if not enough parts
```

## 🚨 **SECURITY CHECKLIST**

Before committing any command code, verify:

- [ ] **Permissions**: All administrative functions check permissions using mixins
- [ ] **Input Validation**: All user inputs are validated for length and format
- [ ] **Sanitization**: User inputs are sanitized before processing
- [ ] **Attribute Access**: No direct `getattr()`/`setattr()` with user-controlled names
- [ ] **Error Handling**: Proper exception handling that doesn't leak system information
- [ ] **Logging**: Security-relevant actions are logged appropriately
- [ ] **File Operations**: Any file operations use secure paths and validation
- [ ] **Database Operations**: Use parameterized queries, avoid string concatenation

## 🔍 **COMMON VULNERABILITIES TO AVOID**

### **1. Permission Bypass**
```python
# BAD: Missing return False
def check_access(self):
    if not has_permission(self.caller):
        self.caller.msg("Access denied")
        # Missing return False here!
    return True
```

### **2. Attribute Injection**
```python
# BAD: User controls attribute name
attr_name = self.args  # User input
setattr(character.db, attr_name, value)  # Can access any attribute!
```

### **3. Path Traversal**
```python
# BAD: User controls file path
filename = self.args
with open(f"logs/{filename}", 'w') as f:  # User could use "../../../etc/passwd"
```

### **4. SQL Injection (if using raw queries)**
```python
# BAD: String concatenation
query = f"SELECT * FROM users WHERE name = '{user_input}'"  # Vulnerable!

# GOOD: Use Django ORM or parameterized queries
User.objects.filter(name=user_input)  # Safe
```

### **5. Information Disclosure**
```python
# BAD: Exposing internal errors
try:
    dangerous_operation()
except Exception as e:
    self.caller.msg(str(e))  # Could leak system information

# GOOD: Generic error messages
try:
    dangerous_operation()
except Exception as e:
    logger.log_err(f"Operation failed: {e}")
    self.caller.msg("Operation failed. Please contact staff.")
```

## 📋 **SECURITY TESTING**

### **Test Cases to Include:**

1. **Permission Tests**: Verify unauthorized users cannot access admin functions
2. **Input Validation**: Test with oversized inputs, special characters, null bytes
3. **Injection Tests**: Test for attribute injection, path traversal, etc.
4. **Error Handling**: Ensure errors don't leak sensitive information
5. **Rate Limiting**: Test for abuse of resource-intensive operations

### **Example Test:**
```python
def test_command_security(self):
    # Test permission bypass
    normal_user = create_character("normal")
    result = normal_user.execute_cmd("+admin_command")
    self.assertIn("permission", result.lower())
    
    # Test input validation
    result = normal_user.execute_cmd(f"+command {'A' * 10000}")
    self.assertIn("too long", result.lower())
    
    # Test injection attempt
    result = normal_user.execute_cmd("+command __dict__=malicious")
    self.assertIn("not allowed", result.lower())
```

## 🔄 **MAINTENANCE**

### **Regular Security Reviews**
- Review new commands for security issues before merging
- Update the `SAFE_DB_ATTRIBUTES` whitelist as needed
- Monitor logs for suspicious activity
- Keep dependencies updated

### **Code Review Checklist**
- [ ] Does this command handle user input safely?
- [ ] Are permissions checked consistently?
- [ ] Could this be abused by malicious users?
- [ ] Are error messages appropriate (not too revealing)?
- [ ] Is logging adequate for security monitoring?

## 📞 **REPORTING SECURITY ISSUES**

If you discover a security vulnerability:

1. **DO NOT** commit the fix immediately to public repositories
2. Report the issue privately to the development team
3. Include steps to reproduce and potential impact
4. Wait for security review before making changes public

---

**Last Updated**: 2024-12-19  
**Version**: 1.0  
**Maintainer**: Development Team

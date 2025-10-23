# Contributing to PyReach

Thank you for your interest in contributing to PyReach! This document provides guidelines for contributing to the project.

## Getting Started

### Development Setup

1. Fork the repository
2. Clone your fork:
   ```bash
   git clone <your-fork-url>
   cd pyreach
   ```
3. Run the installation script:
   ```bash
   # Linux/Mac
   chmod +x install.sh
   ./install.sh
   
   # Windows
   install.bat
   ```

### Development Workflow

1. Create a feature branch:
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. Make your changes

3. Test thoroughly:
   ```bash
   cd PyReach
   evennia test
   evennia start
   # Test in browser and game client
   ```

4. Format your code:
   ```bash
   black PyReach/
   isort PyReach/
   ```

5. Commit with descriptive message:
   ```bash
   git add .
   git commit -m "Add feature: description of changes"
   ```

6. Push to your fork:
   ```bash
   git push origin feature/your-feature-name
   ```

7. Create a Pull Request

## Code Standards

### Python Style

- Follow **PEP 8** style guide
- Use **Black** for formatting (line length 100)
- Use **isort** for import sorting
- Write **docstrings** for all functions and classes
- Add **type hints** where appropriate

### Evennia Best Practices

- Extend Evennia classes properly
- Use Evennia's built-in utilities
- Follow Evennia's typeclass patterns
- Respect Evennia's permission system
- Document commands with proper help text

### Chronicles of Darkness Implementation

- Follow CoDv2 rules accurately
- Reference page numbers in comments
- Implement proper dice mechanics
- Use official terminology
- Document house rules clearly

## What to Contribute

### Welcome Contributions

- **Bug fixes** - Fix any bugs you find
- **New features** - Add game systems or commands
- **Documentation** - Improve or expand docs
- **Wiki content** - Add lore, rules, guides
- **Tests** - Add test coverage
- **UI improvements** - Enhance web interface
- **Performance** - Optimize code

### Please Discuss First

- Major architectural changes
- Breaking changes to existing features
- Large refactors
- Removal of features

Open an issue to discuss before starting work.

## Submitting Changes

### Pull Request Process

1. **Update documentation** - If you add features, document them
2. **Add tests** - Test new functionality
3. **Update CHANGELOG** - Note your changes
4. **Keep commits clean** - Use meaningful commit messages
5. **One feature per PR** - Don't combine unrelated changes

### Commit Message Format

```
Type: Brief description (50 chars or less)

More detailed explanation if needed. Wrap at 72 characters.
Explain what changed and why, not how (the code shows how).

- Bullet points are okay
- Reference issues: Fixes #123
```

**Types:**
- `feat:` - New feature
- `fix:` - Bug fix
- `docs:` - Documentation changes
- `style:` - Code style changes (formatting)
- `refactor:` - Code refactoring
- `test:` - Adding or updating tests
- `chore:` - Maintenance tasks

### Example Commit Messages

```
feat: Add vampire feeding mechanics

Implements blood pool tracking and feeding rolls per CoDv2 rules.
Characters can now use +feed command to hunt and regain vitae.

- Added feed command to vampire cmdset
- Created hunger roll system
- Updated character sheet to show vitae pool

Fixes #42
```

```
fix: Correct willpower calculation for mages

Mages were calculating willpower as Gnosis + Composure instead of
Resolve + Composure per core rules.

Fixes #87
```

## Code Review

All submissions require review. We'll look for:

- **Code quality** - Clean, readable, well-structured
- **Testing** - Adequate test coverage
- **Documentation** - Properly documented
- **Style** - Follows project standards
- **Compatibility** - Works with existing systems
- **Performance** - No significant slowdowns

## Testing Guidelines

### Writing Tests

- Create test files in the same directory as the code
- Use descriptive test names
- Test edge cases and error conditions
- Mock external dependencies
- Keep tests fast and focused

### Running Tests

```bash
# Run all tests
cd PyReach
evennia test

# Run specific app tests
evennia test world.wiki

# Run specific test file
evennia test commands.test_combat
```

## Documentation

### Code Documentation

- **Docstrings**: All functions, classes, and modules
- **Inline comments**: For complex logic
- **Type hints**: For function signatures
- **Examples**: In docstrings when helpful

### User Documentation

- **Wiki pages**: For in-game lore and rules
- **Help entries**: For commands (accessible in-game)
- **README updates**: For installation and setup
- **Guide documents**: For complex systems

## Areas Needing Help

### High Priority

- [ ] More comprehensive tests
- [ ] Additional CoD templates (Mummy, Beast, etc.)
- [ ] Combat system enhancements
- [ ] More wiki content (lore, setting)
- [ ] Character approval workflow

### Medium Priority

- [ ] Additional commands
- [ ] More building tools
- [ ] Economy system
- [ ] Faction management
- [ ] Plot/story tracking

### Lower Priority

- [ ] UI/theme improvements
- [ ] Performance optimization
- [ ] Additional wiki features
- [ ] API development
- [ ] Mobile app integration

## Getting Help

### For Contributors

- **Discord**: Join the Evennia Discord for questions
- **Issues**: Search existing issues before creating new ones
- **Documentation**: Check Evennia docs and PyReach docs
- **Code**: Look at existing implementations for examples

### Resources

- **Evennia Docs**: https://www.evennia.com/docs/
- **Evennia Discord**: https://discord.gg/AJJpcRUhtF
- **CoD Rules**: Chronicles of Darkness 2nd Edition core book
- **Django Docs**: https://docs.djangoproject.com/

## License

By contributing to PyReach, you agree that your contributions will be licensed under the same license as the project (BSD 3-Clause, following Evennia).

## Code of Conduct

### Our Standards

- **Be respectful** - Treat all contributors with respect
- **Be constructive** - Provide helpful feedback
- **Be inclusive** - Welcome newcomers
- **Be patient** - Remember we're all learning

### Unacceptable Behavior

- Harassment or discrimination
- Trolling or insulting comments
- Personal or political attacks
- Publishing others' private information
- Other conduct inappropriate in a professional setting

## Questions?

Feel free to:
- Open an issue for questions
- Ask in the Evennia Discord
- Email the maintainers

---

Thank you for contributing to PyReach! Your help makes this project better for everyone. 🦇✨


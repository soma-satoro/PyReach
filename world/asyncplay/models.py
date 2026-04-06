"""Database models for asynchronous web play actions."""

from django.db import models


class AsyncAction(models.Model):
    """A queued asynchronous action submitted from the web portal."""

    STATUS_PENDING = "pending"
    STATUS_ACKNOWLEDGED = "acknowledged"
    STATUS_RESOLVED = "resolved"
    STATUS_REJECTED = "rejected"

    STATUS_CHOICES = (
        (STATUS_PENDING, "Pending"),
        (STATUS_ACKNOWLEDGED, "Acknowledged"),
        (STATUS_RESOLVED, "Resolved"),
        (STATUS_REJECTED, "Rejected"),
    )

    account = models.ForeignKey(
        "accounts.AccountDB",
        on_delete=models.CASCADE,
        related_name="async_actions",
    )
    character = models.ForeignKey(
        "objects.ObjectDB",
        on_delete=models.CASCADE,
        related_name="async_actions",
    )
    title = models.CharField(max_length=120)
    content = models.TextField()
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default=STATUS_PENDING,
    )
    staff_response = models.TextField(blank=True)
    metadata = models.JSONField(default=dict, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]
        app_label = "asyncplay"

    def __str__(self):
        return f"AsyncAction #{self.id} ({self.status}) - {self.title}"

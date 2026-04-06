"""Database models for asynchronous web play actions."""

from django.db import models
from django.utils import timezone


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


class AsyncScene(models.Model):
    """A slow-paced play-by-post scene."""

    PRIVACY_PRIVATE = "private"
    PRIVACY_OPEN = "open"
    PRIVACY_CHOICES = (
        (PRIVACY_PRIVATE, "Private"),
        (PRIVACY_OPEN, "Open"),
    )

    TYPE_SOCIAL = "social"
    TYPE_EVENT = "event"
    TYPE_VIGNETTE = "vignette"
    TYPE_CHOICES = (
        (TYPE_SOCIAL, "Social"),
        (TYPE_EVENT, "Event"),
        (TYPE_VIGNETTE, "Vignette"),
    )

    PACING_TRADITIONAL = "traditional"
    PACING_DISTRACTED = "distracted"
    PACING_ASYNC = "asynchronous"
    PACING_CHOICES = (
        (PACING_TRADITIONAL, "Traditional"),
        (PACING_DISTRACTED, "Distracted"),
        (PACING_ASYNC, "Asynchronous"),
    )

    creator = models.ForeignKey(
        "accounts.AccountDB",
        on_delete=models.CASCADE,
        related_name="created_async_scenes",
    )
    title = models.CharField(max_length=140)
    notes = models.TextField(blank=True)
    location = models.CharField(max_length=140, blank=True)
    ic_date = models.DateField(default=timezone.localdate)
    scene_type = models.CharField(max_length=20, choices=TYPE_CHOICES, default=TYPE_SOCIAL)
    pacing = models.CharField(max_length=20, choices=PACING_CHOICES, default=PACING_TRADITIONAL)
    privacy = models.CharField(max_length=20, choices=PRIVACY_CHOICES, default=PRIVACY_PRIVATE)
    is_completed = models.BooleanField(default=False)
    is_public_log = models.BooleanField(default=False)
    plot = models.CharField(max_length=140, blank=True)
    tags = models.CharField(max_length=240, blank=True)
    summary = models.TextField(blank=True)
    wiki_log_slug = models.CharField(max_length=200, blank=True)
    participants = models.ManyToManyField("objects.ObjectDB", related_name="async_scenes", blank=True)
    related_scenes = models.ManyToManyField("self", symmetrical=False, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    last_activity_at = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ["-last_activity_at", "-created_at"]
        app_label = "asyncplay"

    def __str__(self):
        return f"Scene #{self.id}: {self.title}"


class AsyncScenePost(models.Model):
    """An individual post/pose inside an async scene."""

    TYPE_POSE = "pose"
    TYPE_OOC = "ooc"
    TYPE_GM_EMIT = "gm_emit"
    TYPE_SCENE_SET = "scene_set"
    TYPE_CHOICES = (
        (TYPE_POSE, "Pose"),
        (TYPE_OOC, "OOC"),
        (TYPE_GM_EMIT, "GM Emit"),
        (TYPE_SCENE_SET, "Scene Set"),
    )

    scene = models.ForeignKey(
        "AsyncScene",
        on_delete=models.CASCADE,
        related_name="posts",
    )
    account = models.ForeignKey(
        "accounts.AccountDB",
        on_delete=models.CASCADE,
        related_name="async_scene_posts",
    )
    character = models.ForeignKey(
        "objects.ObjectDB",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="async_scene_posts",
    )
    post_type = models.CharField(max_length=20, choices=TYPE_CHOICES, default=TYPE_POSE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["created_at"]
        app_label = "asyncplay"

    def __str__(self):
        return f"ScenePost #{self.id} [{self.post_type}]"

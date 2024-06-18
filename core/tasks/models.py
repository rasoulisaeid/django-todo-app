from django.db import models
from django.contrib.auth import get_user_model

# getting user model object
User = get_user_model()

class Task(models.Model):
    """
    Task model representing a to-do task.

    Attributes:
        author (ForeignKey): The author of the task, linked to the Profile model.
        title (TextField): The title of the task.
        status (BooleanField): The completion status of the task (True for completed, False for not completed).
        created_at (DateTimeField): The date and time when the task was created, auto-generated.
        updated_at (DateTimeField): The date and time when the task was last updated, auto-generated.
    """
    author = models.ForeignKey("accounts.User", on_delete=models.CASCADE)
    title = models.TextField()
    status = models.BooleanField(default=False)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        """
        String representation of the Task model.
        
        Returns:
            str: The title of the task.
        """
        return self.title
    
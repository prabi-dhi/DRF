from django.db import models
# from classroom.models import Classroom
from user.models import User
# from subject.models import Subject
# from pygments.lexers import get_lexer_by_name
# from pygments.formatters import HtmlFormatter
# from pygments import highlight

class Student(models.Model):
    name = models.CharField(max_length = 50)
    user = models.ForeignKey(User, on_delete = models.SET_NULL, null= True, blank =True, related_name='students')
    # user = models.OneToOneField(User, on_delete = models.SET_NULL, null= True, blank =True)

    highlighted = models.TextField()

    class Meta:
        db_table = 'STUDENT'
    def __str__(self):
        return self.name
    
# def save(self, *args, **kwargs):
#     lexer = get_lexer_by_name(self.language)
#     linenos = 'table' if self.linenos else False
#     options = {'title': self.title} if self.title else {}
#     formatter = HtmlFormatter(style=self.style, linenos=linenos,
#                               full=True, **options)
#     self.highlighted = highlight(self.code, lexer, formatter)
#     super().save(*args, **kwargs)

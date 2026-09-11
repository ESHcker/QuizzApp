from django.db import models

class test(models.Model):
    CATEGORIES = {
        "General" : "General",
        "Matemáticas" : "Matemáticas",
        "Prueba" : "Prueba",
    }
    title = models.CharField(max_length=80, unique = True)
    description = models.TextField()
    categories = models.CharField(max_length = 30, choices = CATEGORIES)

    def __str__(self):
        return self.description

class question(models.Model):
    text = models.TextField()
    test = models.ForeignKey(test, on_delete=models.CASCADE)

    def __str__(self):
        return self.text

class option(models.Model):
    text = models.CharField(max_length = 200)
    question = models.ForeignKey(question, on_delete=models.CASCADE)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.text

# class qp_answers(models.Model):
#     text = models.CharField(max_length = 200)
#     id_user = models.ForeignKey(Users, on_delete=models.CASCADE)


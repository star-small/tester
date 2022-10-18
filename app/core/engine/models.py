from django.db import models

# Create your models here.
class Question(models.Model):
    text = models.CharField(verbose_name='Текст', max_length=250)
    question_num = models.IntegerField(default=1, unique=True)
    def __str__(self):
        return f"{self.text}"



    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'
        ordering = ['id']

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    text=models.CharField(verbose_name='Ответ', max_length=250)
    right = models.BooleanField(verbose_name='Правильный', default=False)
    def __str__(self):
        return f"{self.question}"

class Test(models.Model):
    title = models.CharField(verbose_name='Тема', max_length=250)
    Questions = models.ManyToManyField(Question)
    def __str__(self):
        return f"{self.title}"
    class Meta:
        verbose_name = 'Тест'
        verbose_name_plural = 'Тесты'
        ordering = ['id']

class Topic(models.Model):
    title = models.CharField(verbose_name='Название', max_length=250)
    theory = models.CharField(verbose_name='Теория', max_length=1000)
    tests = models.ManyToManyField(Test)
    def __str__(self):
        return f"{self.title}"
    class Meta:
        verbose_name = 'Тема'
        verbose_name_plural = 'Темы'
        ordering = ['id']

class Test_Result(models.Model):
    test = models.ForeignKey(Test, on_delete=models.CASCADE)
    result = models.CharField(verbose_name='Результат', max_length=300)
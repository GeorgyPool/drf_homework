from django.db import models


class Сourse(models.Model):
    title = models.CharField(max_length=200, verbose_name="Название курса")
    preview = models.ImageField(
        upload_to="course/preview/", blank=True, null=True, verbose_name="Превью"
    )
    description = models.TextField(blank=True, null=True, verbose_name="Описание курса")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Курс"
        verbose_name_plural = "Курсы"
        ordering = ["title"]


class Lesson(models.Model):
    title = models.CharField(max_length=200, verbose_name="Название")
    description = models.TextField(blank=True, null=True, verbose_name="Описания урока")
    preview = models.ImageField(
        upload_to="lesson/preview/", blank=True, null=True, verbose_name="Превью"
    )
    url_video = models.URLField(blank=True, null=True, verbose_name="Ссылка на видео")
    course = models.ForeignKey(Сourse, related_name="lesson", on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Урок"
        verbose_name_plural = "Уроки"
        ordering = ["title"]

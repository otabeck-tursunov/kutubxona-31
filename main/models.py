from django.db import models


class Talaba(models.Model):
    ism = models.CharField(max_length=255)
    guruh = models.CharField(max_length=50)
    kurs = models.PositiveSmallIntegerField(default=1)
    kitob_soni = models.PositiveSmallIntegerField(default=0)

    def __str__(self):
        return self.ism

    class Meta:
        verbose_name = 'Talaba'
        verbose_name_plural = 'Talabalar'


class Muallif(models.Model):
    JINS_CHOICES = (
        ('Erkak', 'Erkak'),
        ('Ayol', 'Ayol'),
    )
    ism = models.CharField(max_length=255)
    jins = models.CharField(max_length=10, choices=JINS_CHOICES)
    t_sana = models.DateField(blank=True, null=True)
    kitob_soni = models.PositiveSmallIntegerField(blank=True, null=True)
    tirik = models.BooleanField(default=False)

    def __str__(self):
        return self.ism

    class Meta:
        verbose_name = 'Muallif'
        verbose_name_plural = 'Mualliflar'


class Kitob(models.Model):
    nom = models.CharField(max_length=255)
    janr = models.CharField(max_length=255)
    sahifa = models.PositiveSmallIntegerField()
    muallif = models.ForeignKey(Muallif, on_delete=models.SET_NULL, null=True)

    class Meta:
        verbose_name = 'Kitob'
        verbose_name_plural = 'Kitoblar'

    def __str__(self):
        return self.nom


class Kutubxonachi(models.Model):
    ism = models.CharField(max_length=255)
    ish_vaqti = models.TimeField(blank=True, null=True)

    class Meta:
        verbose_name = 'Kutubxonachi'
        verbose_name_plural = 'Kutubxonachilar'

    def __str__(self):
        return self.ism


class Record(models.Model):
    class Meta:
        verbose_name = 'Record'
        verbose_name_plural = 'Recordlar'

    talaba = models.ForeignKey(Talaba, on_delete=models.SET_NULL, null=True)
    kitob = models.ForeignKey(Kitob, on_delete=models.SET_NULL, null=True)
    kutubxonachi = models.ForeignKey(Kutubxonachi, on_delete=models.SET_NULL, null=True)
    olingan_sana = models.DateTimeField(auto_now_add=True)
    qaytardi = models.BooleanField(default=False)
    qaytargan_sana = models.DateField(blank=True, null=True)

    def __str__(self):
        if self.talaba and self.kitob:
            return f"{self.talaba}: {self.kitob}"
        return "-"

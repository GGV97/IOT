from django.db import models

class TemperatureSensor(models.Model):
    tiempo = models.DateTimeField(auto_now_add=True)
    tiempoviaje = models.FloatField()
    altura=models.FloatField()

    def __str__(self):
        return f"{self.tiempoviaje}°C at {self.tiempo}"

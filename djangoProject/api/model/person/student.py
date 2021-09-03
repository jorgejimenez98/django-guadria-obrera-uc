from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from .person import Person
from .municipality import Municipality
from .typeOfStudent import TypeOfStudent
from .typeOfCourse import TypeOfCourse
from .sourceOfIncome import SourceOfIncome
from ..area.career import Career


class Student(Person):
    politicalOrganization = models.CharField(max_length=126)  # UJC o ninguno
    yearOfStudy = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    group = models.PositiveIntegerField(default=0)
    career = models.ForeignKey(Career, on_delete=models.PROTECT, default=None, related_name='students')
    municipality = models.ForeignKey(Municipality, on_delete=models.PROTECT)
    typeOfStudent = models.ForeignKey(TypeOfStudent, on_delete=models.PROTECT)
    typeOfCourse = models.ForeignKey(TypeOfCourse, on_delete=models.PROTECT)
    sourceOfIncome = models.ForeignKey(SourceOfIncome, on_delete=models.PROTECT)

    def __str__(self):
        return '{} | {} | {} | {} | {} | Year {}'.format(self.names, self.surnames, self.state.name,
                                                         self.municipality.name, self.career.name, self.yearOfStudy)


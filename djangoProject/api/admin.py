from django.contrib import admin
from django.contrib.auth.models import Permission
from api.model.area.area import Area
from api.model.area.career import Career
from api.model.area.department import Department
from api.model.area.faculty import Faculty
from api.model.area.universitySeat import UniversitySeat
from api.model.guard.dutyShift import DutyShift
from api.model.guard.guard import Guard
from api.model.guard.studentsGuard import StudentsGuard
from api.model.guard.workersGuard import WorkersGuard
from api.model.officialDistributionOGS import OfficialDistributionOGS
from api.model.officialDistributionAOGS import OfficialDistributionAOGS
from api.model.person.municipality import Municipality
from api.model.person.person import Person
from api.model.person.province import Province
from api.model.person.sourceOfIncome import SourceOfIncome
from api.model.person.state import State
from api.model.person.student import Student
from api.model.person.typeOfCourse import TypeOfCourse
from api.model.person.typeOfStudent import TypeOfStudent
from api.model.person.worker import Worker
from api.model.typeOfUsers.dean import Dean
from api.model.typeOfUsers.departmentHead import DepartmentHead
from api.model.typeOfUsers.facultyProgrammer import FacultyProgrammer
from api.model.typeOfUsers.ppaa import PPAA

admin.site.register(OfficialDistributionOGS)
admin.site.register(OfficialDistributionAOGS)
admin.site.register(Municipality)
admin.site.register(Province)
admin.site.register(Person)
admin.site.register(SourceOfIncome)
admin.site.register(State)
admin.site.register(TypeOfCourse)
admin.site.register(TypeOfStudent)
admin.site.register(Worker)
admin.site.register(Guard)
admin.site.register(StudentsGuard)
admin.site.register(DutyShift)
admin.site.register(WorkersGuard)
admin.site.register(Area)
admin.site.register(Department)
admin.site.register(Faculty)
admin.site.register(Career)
admin.site.register(UniversitySeat)
admin.site.register(Student)
admin.site.register(Permission)
admin.site.register(Dean)
admin.site.register(FacultyProgrammer)
admin.site.register(PPAA)
admin.site.register(DepartmentHead)

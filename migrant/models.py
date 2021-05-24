from django.conf import settings
from django.db import models


class VictimStatus(models.Model):
    name = models.CharField("Название", max_length=255)
    active = models.BooleanField("Активен", default=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Статус пострадавшего/ей"
        verbose_name_plural = "Статусы пострадавших"


class BanOnEntry(models.Model):
    name = models.CharField("Название", max_length=255)
    active = models.BooleanField("Активен", default=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Запрет на въезд"
        verbose_name_plural = "Запреты на въезд"


class Source(models.Model):
    name = models.CharField("Название", max_length=200, help_text='Название')
    active = models.BooleanField("Активен", default=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Источник информации"
        verbose_name_plural = "Источники информации"


class Right(models.Model):
    name = models.CharField("Название", max_length=200, help_text='Название права')
    active = models.BooleanField("Активен", default=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Нарушенное право"
        verbose_name_plural = "Нарушенные права"

class Victim(models.Model):
    name = models.CharField("Название", max_length=200, help_text='Название')
    active = models.BooleanField("Активен", default=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Тип жертвы нарушения"
        verbose_name_plural = "Типы жертв нарушений"

class Gender(models.Model):
    name = models.CharField("Название", max_length=50, help_text='Название')
    active = models.BooleanField("Активен", default=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Пол"
        verbose_name_plural = "Пол"


class Education(models.Model):
    name = models.CharField("Название", max_length=250, help_text='Название')
    active = models.BooleanField("Активен", default=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Образование"
        verbose_name_plural = "Образования"

class Country(models.Model):
    name = models.CharField("Название", max_length=150, help_text='Название страны')
    active = models.BooleanField("Активна", default=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Страна"
        verbose_name_plural = "Страны"

class CountryFrom(models.Model):
    name = models.CharField("Название", max_length=150, help_text='Название страны')
    active = models.BooleanField("Активна", default=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Страна"
        verbose_name_plural = "Страны"


class WayOfArrival(models.Model):
    name = models.CharField("Название", max_length=150, help_text='Способ прибытия')
    active = models.BooleanField("Активна", default=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Способ прибытия"
        verbose_name_plural = "Способы прибытия"

class WayOfFindingWork(models.Model):
    name = models.CharField("Название", max_length=150, help_text='Способ прибытия')
    active = models.BooleanField("Активна", default=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Способ найти работу"
        verbose_name_plural = "Способы найти работу"

class TradeUnionMembership(models.Model):
    name = models.CharField("Название", max_length=150, help_text='Значение')
    active = models.BooleanField("Активна", default=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Членство в профсоюзе"
        verbose_name_plural = "Членства в профсоюзе "

class AgreementDetailYes(models.Model):
    name = models.CharField("Название", max_length=150, help_text='Значение')
    active = models.BooleanField("Активна", default=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Уточнение, если договор есть"
        verbose_name_plural = "Уточнения, если договор есть"

class AgreementDetailNo(models.Model):
    name = models.CharField("Название", max_length=150, help_text='Значение')
    active = models.BooleanField("Активна", default=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Уточнение, если договора нет"
        verbose_name_plural = "Уточнения, если договора нет"

class WorkBookStatus(models.Model):
    name = models.CharField("Название", max_length=150, help_text='Значение')
    active = models.BooleanField("Активна", default=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Есть ли у Вас трудовая книжка?"
        verbose_name_plural = "Есть ли у Вас трудовая книжка?"

class WorkingDayDuration(models.Model):
    name = models.CharField("Длительность", max_length=150, help_text='Длительность')
    active = models.BooleanField("Активна", default=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Длительность рабочего дня"
        verbose_name_plural = "Длительности рабочего дня"

class WayOfGettingSalary(models.Model):
    name = models.CharField("Способ", max_length=150, help_text='Способ')
    active = models.BooleanField("Активна", default=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Способ получения зарплаты"
        verbose_name_plural = "Способы получения зарплаты"


class IndividualInfo(models.Model):
    name = models.CharField("ФИО", max_length=100, help_text='ФИО', default="анонимно")
    #member_of_tradeunion = models.BooleanField("Член профсоюза", default=True)
    gender = models.ForeignKey(Gender, on_delete=models.DO_NOTHING, verbose_name="Пол пострадавшего")
    gender_another = models.CharField("Другое", max_length=50, help_text='Введите значение', null=True,
                                            blank=True)
    age = models.CharField("Возраст пострадавшего", max_length=50, help_text='Возраст пострадавшего')
    contacts = models.CharField("Контактные данные (телефон/адрес) ", max_length=500,
                                help_text='Контактные данные (телефон/адрес) ')
    education = models.ForeignKey(Education, on_delete=models.DO_NOTHING, verbose_name="Образование")
    country = models.ForeignKey(Country, on_delete=models.DO_NOTHING, verbose_name="Страна пребывания пострадавшего")
    countryAnother = models.CharField("Другое", max_length=50, help_text='Введите значение', null=True,
                                            blank=True)
    city_name = models.CharField("Город пребывания пострадавшего", max_length=100, null=True)
    countryFrom = models.ForeignKey(CountryFrom, on_delete=models.DO_NOTHING, verbose_name="Страна исхода пострадавшего")
    countryFromAnother = models.CharField("Другое", max_length=50, help_text='Введите значение', null=True,
                                            blank=True)
    city_name_from = models.CharField("Город/село", max_length=100, null=True)

    wayOfArrival = models.ForeignKey(WayOfArrival, on_delete=models.DO_NOTHING, verbose_name="Как пострадавший приехал в страну пребывания?")
    wayOfArrivalAnother = models.CharField("Другое", max_length=50, help_text='Введите значение', null=True,
                                            blank=True)
    wayOfFindingWork = models.ForeignKey(WayOfFindingWork, on_delete=models.DO_NOTHING, verbose_name="Как пострадавший нашел работу?")
    wayOfFindingWorkAnother = models.CharField("Другое", max_length=50, help_text='Введите значение', null=True,
                                            blank=True)
    hasRegistration=models.CharField("Есть ли у пострадавшего регистрация в стране пребывания?", choices=[('YES', 'Да'),('NO', 'Нет'),], default='YES', max_length=20)
    tradeUnionMembership = models.ForeignKey(TradeUnionMembership, on_delete=models.DO_NOTHING,
                                         verbose_name="Членство в профсоюзе на данный момент ")
    experience = models.CharField("Стаж работы в организации", max_length=50, help_text='Стаж работы в организации')
    hasAgreement = models.CharField("Был ли подписан трудовой договор?",
                                       choices=[('YES', 'Да'), ('NO', 'Нет'), ], max_length=20)
    agreementDetailYes = models.ForeignKey(AgreementDetailYes, on_delete=models.DO_NOTHING,
                                         verbose_name="Уточнение, если договор есть", null=True)
    agreementDetailNo = models.ForeignKey(AgreementDetailNo, on_delete=models.DO_NOTHING,
                                         verbose_name="Уточнение, если договора нет", null=True)
    agreementLang = models.CharField("На каком языке был подписан договор?", max_length=50, help_text='На каком языке был подписан договор?')
    understoodTheContents = models.CharField("Вы поняли содержание договора?",
                                       choices=[('YES', 'Да'), ('NO', 'Нет'), ], max_length=20)
    workBookStatus = models.ForeignKey(WorkBookStatus, on_delete=models.DO_NOTHING,
                                          verbose_name="Есть ли у Вас трудовая книжка? ")
    workingDayDuration = models.ForeignKey(WorkingDayDuration, on_delete=models.DO_NOTHING,
                                          verbose_name="Как долго длится ваш рабочий день?")
    hasOverResponsibilities = models.CharField("Есть ли у вас обязанности сверх договора?",
                                       choices=[('YES', 'Да, говорили одно, а делаем много разной работы'), ('NO', 'Нет, только то, о чем договаривались'), ], max_length=50)
    wayOfGettingSalary = models.ForeignKey(WayOfGettingSalary, on_delete=models.DO_NOTHING,
                                          verbose_name="Как Вы получаете заработную плату?")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Физическое лицо"
        verbose_name_plural = "Физические лица"

class GroupType(models.Model):
    name = models.CharField("Характеристика группы", max_length=150, help_text='Характеристика группы')
    active = models.BooleanField("Активна", default=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Характеристика группы"
        verbose_name_plural = "Характеристики групп"

class MembershipOfGroupPersons(models.Model):
    name = models.CharField("Название", max_length=250, help_text='Название')
    active = models.BooleanField("Активен", default=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Членство в профсоюзе участников группы"
        verbose_name_plural = "Членство в профсоюзе участников группы"

class Intruder(models.Model):
    name = models.CharField("Название", max_length=200, help_text='Название')
    active = models.BooleanField("Активен", default=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Нарушитель"
        verbose_name_plural = "Нарушители"

class PersonGroup(models.Model):
    amount = models.CharField("Количество лиц в группе", max_length=50, help_text='Количество лиц в группе')
    groupType = models.ForeignKey(GroupType, on_delete=models.DO_NOTHING, verbose_name="Характеристика группы")
    workDescription = models.CharField("Количество лиц в группе", max_length=50, help_text='Количество лиц в группе')
    membership = models.ForeignKey(MembershipOfGroupPersons, on_delete=models.DO_NOTHING,
                                   verbose_name="Членство в профсоюзе ")

    def __str__(self):
        return self.groupType

    class Meta:
        verbose_name = "Группа лиц"
        verbose_name_plural = "Группы лиц"

class OwnerShipType(models.Model):
    name = models.CharField("Название", max_length=255)
    active = models.BooleanField("Активен", default=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Форма собственности"
        verbose_name_plural = "Формы собственности"


class EmployeesCount(models.Model):
    # OPTIONS = [
    #     ('COMPANY', 'Для численности сотрудников компании'),
    #     ('STRIKE', 'Для численности участников')
    # ]

    choice = models.CharField("Выбор", max_length=255)
    active = models.BooleanField("Активен", default=True)

    def __str__(self):
        return self.choice

    class Meta:
        verbose_name = "Количество сотрудников предприятия"
        verbose_name_plural = "Количество сотрудников предприятия"

class Company(models.Model):
    company_name = models.CharField("Название", max_length=100, help_text='Название')
    address = models.CharField("Адрес", max_length=100, help_text='Адрес')
    product_type = models.CharField("Вид производимой продукции / Предоставляемые услуги ", max_length=100,
                                    help_text='Вид производимой продукции / Предоставляемые услуги ')
    ownership = models.ForeignKey(OwnerShipType, on_delete=models.DO_NOTHING,
                                  verbose_name="Форма собственности компании")
    company_experience = models.CharField("Время на рынке", max_length=100, help_text='Время на рынке ')
    branch = models.CharField("Отрасль деятельности", max_length=100, help_text='Отрасль деятельности')
    emp_count = models.ForeignKey(EmployeesCount, on_delete=models.DO_NOTHING, verbose_name="Численность работников")
    additional = models.CharField("Иная важная информация", max_length=500, help_text='Иная важная информация ')
    country_from = models.CharField("Страна происхождения компании", max_length=100,
                                    help_text='Страна происхождения кампании')
    is_tnk_member= models.CharField("Является ли эта компания частью ТНК?",
                                       choices=[('YES', 'Да'), ('NO', 'Нет'), ], max_length=20)
    tnk_name = models.CharField("Название ТНК, в которую входит эта компания", max_length=100,
                                help_text='Название ТНК, в которую входит эта компания')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Работодатель (компания)"
        verbose_name_plural = "Работодатели (компании)"

class WorkPurpose(models.Model):
    name = models.CharField("Название", max_length=255)
    active = models.BooleanField("Активен", default=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Цель работы "
        verbose_name_plural = "Цели работы"


class EntrepreneurEmployeesCount(models.Model):
    # OPTIONS = [
    #     ('COMPANY', 'Для численности сотрудников компании'),
    #     ('STRIKE', 'Для численности участников')
    # ]

    choice = models.CharField("Выбор", max_length=255)
    active = models.BooleanField("Активен", default=True)

    def __str__(self):
        return self.choice

    class Meta:
        verbose_name = "Количество сотрудников"
        verbose_name_plural = "Количество сотрудников"

class PayWay(models.Model):
    name = models.CharField("Название", max_length=255)
    active = models.BooleanField("Активен", default=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Способ выдачи"
        verbose_name_plural = "Способы выдачи"

class HireWay(models.Model):
    name = models.CharField("Название", max_length=255)
    active = models.BooleanField("Активен", default=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Способ нанятия на работу"
        verbose_name_plural = "Способы нанятий на работу"

class NatureViolation(models.Model):
    name = models.CharField("Название", max_length=255)
    active = models.BooleanField("Активен", default=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Характер нарушения"
        verbose_name_plural = "Характеры нарушения"

class RightsState(models.Model):
    name = models.CharField("Название", max_length=255)
    active = models.BooleanField("Активен", default=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Ситуация с правами"
        verbose_name_plural = "Ситуации с правами"

class Entrepreneur(models.Model):
    entrepreneur_name = models.CharField("ФИО", max_length=50, help_text='ФИО', default="анонимно")
    entrepreneur_gender = models.ForeignKey(Gender, on_delete=models.DO_NOTHING, verbose_name="Пол")
    entrepreneur_age = models.CharField("Возраст", choices=[('1', '20-35'),('2', '35-50'),('3', '50-70'), ], max_length=50)
    entrepreneur_address = models.CharField("Адрес", max_length=100, help_text='Адрес')
    entrepreneur_workPurpose = models.ManyToManyField(WorkPurpose, verbose_name="Для какой цели нанимает работников?")
    entrepreneur_emp_count = models.ForeignKey(EntrepreneurEmployeesCount, on_delete=models.DO_NOTHING, verbose_name="Численность работников")
    entrepreneur_doAgreement= models.CharField("Оформляет ли он трудовые договора/соглашения с работниками? ",
                                       choices=[('YES', 'Да'), ('NO', 'Нет'), ], max_length=20)
    entrepreneur_payWay = models.ForeignKey(PayWay, on_delete=models.DO_NOTHING,
                                  verbose_name="Как выдает заработную плату?")
    entrepreneur_hireWay = models.ManyToManyField(HireWay, verbose_name="Как нанимает работников?")
    entrepreneur_hireWayAnother = models.CharField("Другое", max_length=50, help_text='Введите значение', null=True,
                                         blank=True)


    def __str__(self):
        return self.choice

    class Meta:
        verbose_name = "Работодатель (частное лицо)"
        verbose_name_plural = "Работодатели (частное лицо)"


class VictimSituation(models.Model):
    name = models.CharField("Название", max_length=255)
    active = models.BooleanField("Активен", default=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Ситуация с потерпевшим(и)"
        verbose_name_plural = "Ситуации с потерпевшим(и)"

class TradeUnionSituation(models.Model):
    name = models.CharField("Название", max_length=255)
    active = models.BooleanField("Активен", default=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Профсоюз на месте работы после произошедшего"
        verbose_name_plural = "Профсоюзы на месте работы после произошедшего "

class ViolationType(models.Model):
    name = models.CharField("Название", max_length=255)
    active = models.BooleanField("Активен", default=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Тип нарушений трудовых прав"
        verbose_name_plural = "Типы нарушений трудовых прав"

class ChangesInSalary(models.Model):
    name = models.CharField("Название", max_length=255)
    active = models.BooleanField("Активен", default=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Изменение в зарплате"
        verbose_name_plural = "Изменения в зарплате"

class TradeUnionCount(models.Model):
    # OPTIONS = [
    #     ('COMPANY', 'Для численности сотрудников компании'),
    #     ('STRIKE', 'Для численности участников')
    # ]

    choice = models.CharField("Выбор", max_length=255)
    active = models.BooleanField("Активен", default=True)

    def __str__(self):
        return self.choice

    class Meta:
        verbose_name = "Численность профсоюза после произошедшего"
        verbose_name_plural = "Численность профсоюза после произошедшего"

class CasePhoto(models.Model):
    file = models.FileField()
    card = models.ForeignKey("Case", on_delete=models.DO_NOTHING, null=True)

    def __str__(self):
        return self.file

    class Meta:
        verbose_name = "Фото/видео/документы "
        verbose_name_plural = "Фото/видео/документы "


class CaseFile(models.Model):
    file = models.FileField()
    card = models.ForeignKey("Case", on_delete=models.DO_NOTHING, null=True)

    def __str__(self):
        return self.file

    class Meta:
        verbose_name = "Кейсы, связанные с забастовкой"
        verbose_name_plural = "Кейсы, связанные с забастовкой"


# Create your models here.
class Case(models.Model):
    date_create = models.DateTimeField("Дата создания", auto_now_add=True)
    date_update = models.DateTimeField("Дата последних изменений", auto_now=True)

    case_name = models.CharField("Название (описание) карточки", max_length=30, help_text='Название (описание) карточки')
    victim_status = models.ForeignKey(VictimStatus, on_delete=models.DO_NOTHING, verbose_name="Статус пострадавшего/ей")
    banOnEntry = models.ForeignKey(BanOnEntry, on_delete=models.DO_NOTHING, verbose_name="Запрет на въезд", null=False)
    banOnEntryAnother = models.CharField("Другое", max_length=50, help_text='Введите значение', null=True,
                                         blank=True)
    source = models.ManyToManyField(Source, verbose_name="Источник информации о нарушении")
    source_url = models.CharField("Источник информации", max_length=255, null=True, blank=True)
    source_content = models.TextField("Текст статьи/сообщения ", null=True, blank=True)
    violated_right = models.ManyToManyField(Right,verbose_name="Какое право нарушено?")
    violatedRightAnother = models.CharField("Другое", max_length=50, help_text='Введите значение', null=True,
                                         blank=True)
    case_date = models.DateTimeField("Дата создания", auto_now_add=True)
    start_date = models.DateTimeField("Дата начала нарушения", auto_now_add=True)
    end_date = models.DateTimeField("Дата конца нарушения", auto_now_add=True)
    victim = models.ForeignKey(Victim, on_delete=models.DO_NOTHING, verbose_name="В отношении кого совершено нарушение")
    individualInfo = models.ForeignKey(IndividualInfo, on_delete=models.DO_NOTHING, verbose_name="физическое лицо", null=True)
    personGroupInfo = models.ForeignKey(PersonGroup, on_delete=models.DO_NOTHING, verbose_name="Группа лиц", null=True)
    intruder = models.ManyToManyField(Intruder, verbose_name="Кем было совершено нарушение", null=False,
                                 default=None)
    government_agency_name = models.CharField("Название государственного органа", max_length=200, null=True,blank=True)
    local_agency_name = models.CharField("Название органа местного самоуправления", max_length=500, null=True, blank=True)
    police_agency_name = models.CharField("Название правоохранительного органа", max_length=500, null=True,blank=True)
    control_agency_name = models.CharField("Название контролирующего органа", max_length=500, null=True,blank=True)
    company = models.ForeignKey(Company, on_delete=models.DO_NOTHING, verbose_name="Работодатель(компания)", null=True)
    entrepreneur = models.ManyToManyField(Entrepreneur, verbose_name="Работодатель(Частное лицо)", null=True)

    case_additional = models.TextField('Укажите точные имена, даты, места событий', max_length=200, default="")
    story = models.TextField('Укажите ПОСЛЕДОВАТЕЛЬНО, что произошло', max_length=1800,
                             help_text='Параллельно указывайте, чем подтверждаются эти факты (если есть приложения,'
                                       ' укажите сразу номера и названия соответствующих приложений)', default="")
    actions = models.TextField('Опишите, какие действия предприняты профсоюзом/правозащитной организацией. Параллельно указывайте, чем подтверждаются эти факты (если есть приложения, укажите сразу номера и названия соответствующих приложений) ', max_length=200, default="")
    final = models.TextField('Чем завершилась ситуация (если завершилась) или состояние в текущий момент', max_length=1800, default="")

    violation_nature = models.ForeignKey(NatureViolation, on_delete=models.DO_NOTHING,
                                         verbose_name="Характер нарушения", null=True)
    rights_state = models.ForeignKey(RightsState, on_delete=models.DO_NOTHING, verbose_name="Ситуация с правами",
                                     null=True)
    rights_state_another=models.CharField("Другое", max_length=50, help_text='Введите значение', null=True,
                                              blank=True)
    victim_situation=models.ForeignKey(VictimSituation,on_delete=models.DO_NOTHING, verbose_name="Ситуация с потерпевшим(и)", null=True)
    victim_situation_another=models.CharField("Другое", max_length=50, help_text='Введите значение', null=True,
                                              blank=True)
    tradeUnionSituation=models.ForeignKey(TradeUnionSituation,on_delete=models.DO_NOTHING, verbose_name="Профсоюз на месте работы после произошедшего ", null=True)
    tradeUnionSituation_another=models.CharField("Другое", max_length=50, help_text='Введите значение', null=True,
                                              blank=True)
    tradeUnionCount = models.ForeignKey(TradeUnionCount, on_delete=models.DO_NOTHING,
                                            verbose_name="Численность профсоюза после произошедшего", null=True)

    frequent_problems = models.TextField('С какими на ваш взгляд проблемами чаще всего сталкиваются мигранты и почему?',
                             max_length=1800, default="")
    decision = models.TextField('Какие по вашему мнению есть пути решения этих проблем?',
                             max_length=1800, default="")
    advice = models.TextField('Какая помощь на ваш взгляд необходима мигрантам?',
                             max_length=1800, default="")

    has_violation_in_covid = models.CharField("Были ли нарушены Ваши трудовые права во время пандемии?",
                                       choices=[('YES', 'Да'), ('NO', 'Нет'), ], default='YES', max_length=20)
    violationType=models.ForeignKey(ViolationType,on_delete=models.DO_NOTHING, verbose_name="С какими нарушениями трудовых прав вы столкнулись из-за COVID-19?", null=True)
    violationType_another=models.CharField("Другое", max_length=50, help_text='Введите значение', null=True,
                                              blank=True)

    changesInSalary=models.ForeignKey(ChangesInSalary,on_delete=models.DO_NOTHING, verbose_name="Как изменились Ваши доходы из-за COVID-19?", null=True)
    changesInSalary_another=models.CharField("Другое", max_length=50, help_text='Введите значение', null=True,
                                              blank=True)

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING,
                                 verbose_name="Монитор")
    active = models.BooleanField("Активен", default=True)
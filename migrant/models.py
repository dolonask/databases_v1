from django.conf import settings
from django.db import models
from django.contrib.auth.models import User


class Employee(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    country = models.ForeignKey("Country",on_delete=models.DO_NOTHING, verbose_name="Страна пользователя")

    def __str__(self):
        return self.user.first_name

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"


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


class InfoSource(models.Model):
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


class IndividualCountry(models.Model):
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


class Country(models.Model):
    name = models.CharField("Название", max_length=255)
    active = models.BooleanField("Активен", default=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Страна"
        verbose_name_plural = "Страны"


class Region(models.Model):
    name = models.CharField("Название", max_length=255, blank=False)
    active = models.BooleanField("Активен", default=True)
    country = models.ForeignKey(Country, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Регион"
        verbose_name_plural = "Регионы"


class IndividualInfo(models.Model):
    is_anonim = models.CharField("анонимно", choices=[('YES', 'Да'), ('NO', 'Нет'), ], max_length=20)
    name = models.CharField("ФИО", max_length=100, help_text='ФИО')
    #member_of_tradeunion = models.BooleanField("Член профсоюза", default=True)
    gender = models.ForeignKey(Gender, on_delete=models.DO_NOTHING, verbose_name="Пол пострадавшего")
    gender_another = models.CharField("Другое", max_length=50, help_text='Введите значение', null=True,
                                            blank=True, )
    individual_age = models.CharField("Возраст пострадавшего", max_length=50)
    contacts = models.CharField("Контактные данные (телефон/адрес) ", max_length=500,
                                help_text='Контактные данные (телефон/адрес) ', )
    education = models.ForeignKey(Education, on_delete=models.DO_NOTHING, verbose_name="Образование")
    individual_country = models.ForeignKey(IndividualCountry, on_delete=models.DO_NOTHING, verbose_name="Страна пребывания пострадавшего")
    countryAnother = models.CharField("Другое", max_length=50, help_text='Введите значение', null=True,
                                            blank=True, )
    city_name = models.CharField("Город пребывания пострадавшего", max_length=100, null=True)
    countryFrom = models.ForeignKey(CountryFrom, on_delete=models.DO_NOTHING, verbose_name="Страна исхода пострадавшего")
    countryFromAnother = models.CharField("Другое", max_length=50, help_text='Введите значение', null=True,
                                            blank=True, )
    city_name_from = models.CharField("Город/село", max_length=100, null=True, )

    wayOfArrival = models.ForeignKey(WayOfArrival, on_delete=models.DO_NOTHING, verbose_name="Как пострадавший приехал в страну пребывания?")
    wayOfArrivalAnother = models.CharField("Другое", max_length=50, help_text='Введите значение', null=True,
                                            blank=True, )
    wayOfFindingWork = models.ForeignKey(WayOfFindingWork, on_delete=models.DO_NOTHING, verbose_name="Как пострадавший нашел работу?")
    wayOfFindingWorkAnother = models.CharField("Другое", max_length=50, help_text='Введите значение', null=True,
                                            blank=True, )
    hasRegistration=models.CharField("Есть ли у пострадавшего регистрация в стране пребывания?", choices=[('YES', 'Да'),('NO', 'Нет'),], max_length=20)
    tradeUnionMembership = models.ForeignKey(TradeUnionMembership, on_delete=models.DO_NOTHING,
                                         verbose_name="Членство в профсоюзе на данный момент ")
    experience = models.CharField("Стаж работы в организации", max_length=50, help_text='Стаж работы в организации')
    hasAgreement = models.CharField("Был ли подписан трудовой договор?",
                                       choices=[('YES', 'Да'), ('NO', 'Нет'), ], max_length=20)
    agreementDetailYes = models.ForeignKey(AgreementDetailYes, on_delete=models.DO_NOTHING,
                                         verbose_name="Уточнение, если договор есть", null=True, blank=True)
    agreementDetailNo = models.ForeignKey(AgreementDetailNo, on_delete=models.DO_NOTHING,
                                         verbose_name="Уточнение, если договора нет", null=True, blank=True)
    agreementLang = models.CharField("На каком языке был подписан договор?", max_length=50, help_text='На каком языке был подписан договор?', )
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
    workDescription = models.CharField("Опишите чем занимаются люди в организации, права которых нарушены", max_length=50)
    membership = models.ForeignKey(MembershipOfGroupPersons, on_delete=models.DO_NOTHING,
                                   verbose_name="Членство в профсоюзе ")

    def __str__(self):
        return self.groupType.name

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
    company_name = models.CharField("Название компании ", max_length=100, help_text='Название', )
    address = models.CharField("Место нахождения (адрес\телефон)", max_length=100, help_text='Адрес', )
    ownership = models.ForeignKey(OwnerShipType, on_delete=models.DO_NOTHING,
                                  verbose_name="Форма собственности компании")
    country_from = models.CharField("Страна происхождения компании", max_length=100,
                                    help_text='Страна происхождения кампании', )
    is_tnk_member= models.CharField("Является ли эта компания частью ТНК?",
                                       choices=[('YES', 'Да'), ('NO', 'Нет'), ], max_length=20)
    tnk_name = models.CharField("Название ТНК, в которую входит эта компания", max_length=100,
                                help_text='Название ТНК, в которую входит эта компания', )
    branch = models.CharField("Отрасль деятельности", max_length=50)
    product_type = models.CharField("Вид производимой продукции / Предоставляемые услуги ", max_length=100,
                                    help_text='Вид производимой продукции / Предоставляемые услуги ', )

    company_experience = models.CharField("Время работы на рынке (в стране, где произошел случай)", max_length=100)

    emp_count = models.ForeignKey(EmployeesCount, on_delete=models.DO_NOTHING, verbose_name="Численность работников")
    additional = models.CharField("Иная важная информация (Другие компании, связанные с ней, головная компания, подрядчики, поставщики и пр.) ", max_length=200, help_text='Иная важная информация ', null=True, blank=True)

    def __str__(self):
        return self.company_name

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
    entrepreneur_is_anonim = models.CharField("Аноним?", choices=[('YES', 'Да'), ('NO', 'Нет'), ], max_length=20)
    entrepreneur_name = models.CharField("ФИО", max_length=50, help_text='ФИО', )
    # entrepreneur_is_anonim = models.BooleanField("Аноним?", default=False)
    # entrepreneur_gender = models.ForeignKey(Gender, on_delete=models.DO_NOTHING, verbose_name="Пол")
    entrepreneur_gender = models.CharField("Пол", choices=[('FEMALE', 'Женский'),('MALE', 'Мужской')],max_length=50)
    entrepreneur_age = models.CharField("Возраст", choices=[('1', '20-35'),('2', '35-50'),('3', '50-70'), ], max_length=50)
    entrepreneur_address = models.CharField("Адрес", max_length=100, help_text='Адрес', )
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
        return self.entrepreneur_name

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
    choice = models.CharField("Выбор", max_length=255)
    active = models.BooleanField("Активен", default=True)

    def __str__(self):
        return self.choice

    class Meta:
        verbose_name = "Численность профсоюза после произошедшего"
        verbose_name_plural = "Численность профсоюза после произошедшего"
    # OPTIONS = [
    #     ('COMPANY', 'Для численности сотрудников компании'),
    #     ('STRIKE', 'Для численности участников')
    # ]


# Create your models here.
class Case(models.Model):
    date_create = models.DateTimeField("Дата создания", auto_now_add=True)
    date_update = models.DateTimeField("Дата последних изменений", auto_now=True)
    case_name = models.CharField("Название (описание) карточки", max_length=30, help_text='Название (описание) карточки')
    country = models.ForeignKey(Country, on_delete=models.DO_NOTHING, verbose_name="Страна")
    region = models.ForeignKey(Region, on_delete=models.DO_NOTHING, verbose_name="Регион")
    victim_status = models.ForeignKey(VictimStatus, on_delete=models.DO_NOTHING, verbose_name="Статус пострадавшего/ей")
    banOnEntry = models.ForeignKey(BanOnEntry, on_delete=models.DO_NOTHING,
                                   verbose_name="Есть ли у вас запрет на въезд?", null=False)
    banned_country = models.CharField("В какую страну?", max_length=50, null=True, blank=True)
    banOnEntryAnother = models.CharField("Другое", max_length=50, help_text='Введите значение', null=True, blank=True)
    source = models.ManyToManyField(InfoSource, verbose_name="Источник информации о нарушении")
    source_url = models.CharField("Источник информации", max_length=255, null=True, blank=True, )
    source_content = models.TextField("Текст статьи/сообщения", null=True, blank=True)
    violated_right = models.ManyToManyField(Right, verbose_name="Какое право нарушено?")
    violatedRightAnother = models.CharField("Другое", max_length=50, help_text='Введите значение', null=True, blank=True)
    case_date = models.DateTimeField("Дата создания", auto_now_add=True)
    start_date = models.DateTimeField("Дата начала нарушения")
    end_date = models.DateTimeField("Дата конца нарушения", null=True, blank=True)
    victim = models.ForeignKey(Victim, on_delete=models.DO_NOTHING, verbose_name="В отношении кого совершено нарушение")
    individualInfo = models.ForeignKey(IndividualInfo, on_delete=models.DO_NOTHING, verbose_name="физическое лицо", null=True)
    personGroupInfo = models.ForeignKey(PersonGroup, on_delete=models.DO_NOTHING, verbose_name="Группа лиц", null=True)
    intruder = models.ManyToManyField(Intruder, verbose_name="Кем было совершено нарушение", null=False)
    government_agency_name = models.CharField("Название государственного органа", max_length=200, null=True, blank=True)
    local_agency_name = models.CharField("Название органа местного самоуправления", max_length=500, null=True, blank=True)
    police_agency_name = models.CharField("Название правоохранительного органа", max_length=500, null=True, blank=True)
    control_agency_name = models.CharField("Название контролирующего органа", max_length=500, null=True, blank=True)
    company = models.ForeignKey(Company, on_delete=models.DO_NOTHING, verbose_name="Работодатель(компания)", null=True)
    entrepreneur = models.ForeignKey(Entrepreneur, on_delete=models.DO_NOTHING,
                                     verbose_name="Работодатель(Частное лицо)", null=True)
    case_additional = models.TextField('Укажите точные имена, даты, места событий', max_length=200)
    story = models.TextField('Укажите ПОСЛЕДОВАТЕЛЬНО, что произошло. Параллельно указывайте, '
                             'чем подтверждаются эти факты (если есть приложения, укажите сразу '
                             'номера и названия соответствующих приложений)', max_length=1800)
    actions = models.TextField('Опишите, какие действия предприняты профсоюзом/правозащитной организацией. '
                               'Параллельно указывайте, чем подтверждаются эти факты (если есть приложения, '
                               'укажите сразу номера и названия соответствующих приложений) ', max_length=200)
    final = models.TextField('Чем завершилась ситуация (если завершилась) или состояние в текущий момент', max_length=1800)
    violation_nature = models.ForeignKey(NatureViolation, on_delete=models.DO_NOTHING, verbose_name="Характер нарушения", null=True)
    rights_state = models.ForeignKey(RightsState, on_delete=models.DO_NOTHING, verbose_name="Ситуация с правами", null=True)
    rights_state_another = models.CharField("Другое", max_length=50, help_text='Введите значение', null=True, blank=True)
    victim_situation = models.ForeignKey(VictimSituation,on_delete=models.DO_NOTHING,
                                         verbose_name="Ситуация с потерпевшим(и)", null=True)
    victim_situation_another = models.CharField("Другое", max_length=50, help_text='Введите значение', null=True, blank=True)
    tradeUnionSituation = models.ForeignKey(TradeUnionSituation,on_delete=models.DO_NOTHING,
                                            verbose_name="Профсоюз на месте работы после произошедшего", blank=True, null=True)
    tradeUnionSituation_another = models.CharField("Другое", max_length=50, help_text='Введите значение', null=True, blank=True)
    tradeUnionCount = models.ForeignKey(TradeUnionCount, on_delete=models.DO_NOTHING,
                                        verbose_name="Численность профсоюза после произошедшего", blank=True, null=True)
    case_additional_info = models.CharField("Информация", max_length=5000, null=True, blank=True)
    frequent_problems = models.TextField('С какими на ваш взгляд проблемами чаще всего сталкиваются мигранты и почему?',
                                         max_length=1800, blank=True, null=True)
    decision = models.TextField('Какие по вашему мнению есть пути решения этих проблем?', max_length=1800, blank=True, null=True)
    advice = models.TextField('Какая помощь на ваш взгляд необходима мигрантам?', max_length=1800, blank=True, null=True)
    has_violation_in_covid = models.CharField("Были ли нарушены Ваши трудовые права во время пандемии?",
                                              choices=[('YES', 'Да'), ('NO', 'Нет'), ], max_length=20)
    violationType = models.ForeignKey(ViolationType, on_delete=models.DO_NOTHING,
                                      verbose_name="С какими нарушениями трудовых прав вы столкнулись из-за COVID-19?", null=True)
    violationType_another = models.CharField("Другое", max_length=50, help_text='Введите значение', null=True, blank=True)
    changesInSalary = models.ForeignKey(ChangesInSalary,on_delete=models.DO_NOTHING,
                                        verbose_name="Как изменились Ваши доходы из-за COVID-19?", null=True)
    changesInSalary_another = models.CharField("Другое", max_length=50, help_text='Введите значение', null=True, blank=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING, verbose_name="Монитор")
    active = models.BooleanField("Активен", default=True)
    comment = models.TextField('Комментарии для монитора',max_length=500, blank= True, null= True)

    def __str__(self):
        return self.case_name

    class Meta:
        verbose_name = 'Кейс мигрант'
        verbose_name_plural = 'Кейсы мигранты'


def files_location(instance, filename):
    return "%s/%s/%s" %("files/migrant", instance.card.pk, filename)


def photos_location(instance, filename):
    return "%s/%s/%s" %("photos/migrant", instance.card.pk, filename)


class CasePhoto(models.Model):
    card = models.ForeignKey(Case, on_delete=models.DO_NOTHING, null=True)
    photo = models.FileField("Фото/видео/документы",upload_to=photos_location)

    def __str__(self):
        return self.photo

    class Meta:
        verbose_name = "Фото/видео/документы "
        verbose_name_plural = "Фото/видео/документы "


class CaseFile(models.Model):
    card = models.ForeignKey(Case, on_delete=models.DO_NOTHING, null=True)
    file = models.FileField("Кейсы, связанные с забастовкой", upload_to=files_location)

    def __str__(self):
        return self.file

    class Meta:
        verbose_name = "Кейсы, связанные с забастовкой"
        verbose_name_plural = "Кейсы, связанные с забастовкой"


class CaseComment(models.Model):
    comment = models.TextField("Комментарий")
    active = models.BooleanField("Активен", default=True)
    date_create = models.DateTimeField("Дата создания", auto_now_add=True)
    case = models.ForeignKey(Case, on_delete=models.DO_NOTHING)

    class Meta:
        verbose_name = "Комментарий к мигранту"
        verbose_name_plural = "Комментарии к мигрантам"

from django.db import models


# Create your models here.


class Country(models.Model):
    name = models.CharField("Название", max_length=150, help_text='Название страны')
    active = models.BooleanField("Активна", default=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Страна"
        verbose_name_plural = "Страны"


class Region(models.Model):
    name = models.CharField("Название", max_length=150, help_text='Название страны')
    active = models.BooleanField("Активен", default=True)
    country = models.ForeignKey(Country, on_delete=models.DO_NOTHING, verbose_name="Страна")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Регион"
        verbose_name_plural = "Регионы"


class Source(models.Model):
    name = models.CharField("Название", max_length=200, help_text='Название страны')
    active = models.BooleanField("Активен", default=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Источник информации"
        verbose_name_plural = "Источники информации"


class GroupOfRights(models.Model):
    name = models.CharField("Название", max_length=200, help_text='Название')
    active = models.BooleanField("Активен", default=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Группа прав"
        verbose_name_plural = "Группы прав"


class RightsViolation(models.Model):
    name = models.CharField("Название", max_length=250)
    active = models.BooleanField("Активен", default=True)
    groupOfRights = models.ForeignKey(GroupOfRights, on_delete=models.DO_NOTHING, verbose_name="Группа прав")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Нарушение прав"
        verbose_name_plural = "Нарушения прав"


class RightsViolationCase(models.Model):
    name = models.CharField("Название", max_length=250, help_text='Название')
    active = models.BooleanField("Активен", default=True)
    rightsViolation = models.ForeignKey(RightsViolation, on_delete=models.DO_NOTHING, verbose_name="Нарушение прав")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Тип нарушения права"
        verbose_name_plural = "Типы нарушения прав"


class Victim(models.Model):
    name = models.CharField("Название", max_length=250, help_text='Название')
    active = models.BooleanField("Активен", default=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Лицо или организация"
        verbose_name_plural = "Лица или организации"


class TradeUnionInfo(models.Model):
    name = models.CharField("Объединение ", max_length=500, help_text='Название федерации, конфедерации профсоюзов')
    branch_name = models.CharField("Название отраслевой профсоюзной организации", max_length=500,
                                   help_text='Название отраслевой профсоюзной организации')
    victim_name = models.CharField("Название организации, права которой были нарушены ", max_length=500,
                                   help_text='федерация, отраслевое объединение, первичная организация')
    contacts = models.CharField("Контактные данные этой организации", max_length=500,
                                help_text='электронная почта, адрес\телефон')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Профсоюзная организация"
        verbose_name_plural = "Профсоюзные организации"


class Education(models.Model):
    name = models.CharField("Название", max_length=250, help_text='Название')
    active = models.BooleanField("Активен", default=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Образование"
        verbose_name_plural = "Образования"


class MaritalStatus(models.Model):
    name = models.CharField("Название", max_length=250, help_text='Название')
    active = models.BooleanField("Активен", default=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Состояние в браке"
        verbose_name_plural = "Состояния в браке"


class Gender(models.Model):
    name = models.CharField("Название", max_length=50, help_text='Название')
    active = models.BooleanField("Активен", default=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Пол"
        verbose_name_plural = "Пол"


class AgreementDetail(models.Model):
    name = models.CharField("Название", max_length=200, help_text='Название')
    active = models.BooleanField("Активен", default=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Детали договора"
        verbose_name_plural = "Детали договора"


class IndividualInfo(models.Model):
    name = models.CharField("ФИО", max_length=50, help_text='ФИО', default="анонимно")
    member_of_tradeunion = models.BooleanField("Член профсоюза", default=True)
    gender = models.ForeignKey(Gender, on_delete=models.DO_NOTHING, verbose_name="Пол пострадавшего")
    age = models.CharField("Возраст пострадавшего", max_length=50, help_text='Возраст пострадавшего')
    education = models.ForeignKey(Education, on_delete=models.DO_NOTHING, verbose_name="Образование")
    marital_status = models.ForeignKey(MaritalStatus, on_delete=models.DO_NOTHING, verbose_name="Состояние в браке")
    position = models.CharField("Должность в организации", max_length=50, help_text='Должность в организации')
    experience = models.CharField("Стаж работы в организации", max_length=50, help_text='Стаж работы в организации')
    is_official = models.BooleanField("Было ли официальное трудоустройство? ", default=True)
    has_agreement = models.BooleanField("Был ли подписан трудовой договор?", default=False)
    agreementDetail = models.ForeignKey(AgreementDetail, on_delete=models.DO_NOTHING, verbose_name="Детали договора")
    case = models.ForeignKey("Case", on_delete=models.CASCADE, verbose_name="Карточка")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Физическое лицо"
        verbose_name_plural = "Физические лица"

# class TradeunionMembership(models.Model):
#     name = models.CharField("Значение", max_length=100)
#     active = models.BooleanField("Активен", default=True)
#
#     class Meta:
#         verbose_name = "Членство в профсоюзе"
#         verbose_name_plural = "Членства в профсоюзе "
#
#     def __str__(self):
#         return self.name


class GroupType(models.Model):
    name = models.CharField("Название", max_length=250, help_text='Название')
    active = models.BooleanField("Активен", default=True)

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


class GroupOfPersons(models.Model):
    amount = models.CharField("Количество лиц в группе ", max_length=50, help_text='Количество лиц в группе ')
    type = models.ForeignKey(GroupType, on_delete=models.DO_NOTHING, verbose_name="Характеристика группы")
    type_another = models.CharField("Другое", max_length=50, null=True)
    membership = models.ForeignKey(MembershipOfGroupPersons, on_delete=models.DO_NOTHING,
                                   verbose_name="Членство в профсоюзе ")
    membership_another=models.CharField("Другое", max_length=50, null=True)

    def __str__(self):
        return self.amount

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


class Company(models.Model):
    name = models.CharField("Название", max_length=100, help_text='Название')
    address = models.CharField("Адрес", max_length=100, help_text='Адрес')
    product_type = models.CharField("Вид производимой продукции / Предоставляемые услуги ", max_length=100,
                                    help_text='Вид производимой продукции / Предоставляемые услуги ')
    ownership = models.ForeignKey(OwnerShipType, on_delete=models.DO_NOTHING,
                                  verbose_name="Форма собственности компании")
    experience = models.CharField("Время на рынке", max_length=100, help_text='Время на рынке ')
    branch = models.CharField("Отрасль деятельности", max_length=100, help_text='Отрасль деятельности')
    emp_count = models.ForeignKey(EmployeesCount, on_delete=models.DO_NOTHING, verbose_name="Численность работников")
    additional = models.CharField("Иная важная информация ", max_length=500, help_text='Иная важная информация ')
    country_from = models.CharField("Страна происхождения компании", max_length=100,
                                    help_text='Страна происхождения кампании')
    is_tnk_member = models.BooleanField("Является ли эта компания частью ТНК?", default=False)
    tnk_name = models.CharField("Название ТНК, в которую входит эта компания", max_length=100,
                                help_text='Название ТНК, в которую входит эта компания')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Работодатель (компания)"
        verbose_name_plural = "Работодатели (компании)"


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

class TradeUnionRight(models.Model):
    name = models.CharField("Название", max_length=255)
    active = models.BooleanField("Активен", default=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Нарушение в сфере профсоюзных прав и гражданских свобод"
        verbose_name_plural = "Нарушения в сфере профсоюзных прав и гражданских свобод"

class TradeUnionCrime(models.Model):
    name = models.CharField("Название", max_length=255)
    active = models.BooleanField("Активен", default=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Обвинения в преступном поведении в связи с профсоюзной деятельностью"
        verbose_name_plural = "Обвинения в преступном поведении в связи с профсоюзной деятельностью"

class MeetingsRight(models.Model):
    name = models.CharField("Название", max_length=255)
    active = models.BooleanField("Активен", default=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Нарушение права на проведение собраний и демонстраций"
        verbose_name_plural = "Нарушения права на проведение собраний и демонстраций"

class TradeUnionBuildingsRight(models.Model):
    name = models.CharField("Название", max_length=255)
    active = models.BooleanField("Активен", default=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Защита профсоюзных помещений и имущества профсоюзов"
        verbose_name_plural = "Защиты профсоюзных помещений и имущества профсоюзов"

class CreateOrganizationRight(models.Model):
    name = models.CharField("Название", max_length=255)
    active = models.BooleanField("Активен", default=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Создание организации без предварительного разрешения"
        verbose_name_plural = "Создания организации без предварительного разрешения"


class CreateTradeUnionRight(models.Model):
    name = models.CharField("Название", max_length=255)
    active = models.BooleanField("Активен", default=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Создание профсоюзов без предварительного разрешения"
        verbose_name_plural = "Создания профсоюзов без предварительного разрешения"

class ElectionsRight(models.Model):
    name = models.CharField("Название", max_length=255)
    active = models.BooleanField("Активен", default=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Нарушение права свободно выбирать своих представителей"
        verbose_name_plural = "Нарушения права свободно выбирать своих представителей"

class TradeUnionActivityRight(models.Model):
    name = models.CharField("Название", max_length=255)
    active = models.BooleanField("Активен", default=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Нарушение права профсоюза организовывать деятельность своего аппарата"
        verbose_name_plural = "Нарушения права профсоюза организовывать деятельность своего аппарата"

class CreateStrikeRight(models.Model):
    name = models.CharField("Название", max_length=255)
    active = models.BooleanField("Активен", default=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Нарушение права на забастовку"
        verbose_name_plural = "Нарушения прав на забастовку"

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




class Case(models.Model):
    date_create = models.DateTimeField("Дата создания", auto_now_add=True)
    date_update = models.DateTimeField("Дата последних изменений", auto_now=True)

    name = models.CharField("Название (описание) карточки", max_length=50, help_text='Название (описание) карточки')
    source = models.ManyToManyField(Source, verbose_name="Источник информации о нарушении")
    source_url = models.CharField("Источник информации", max_length=255, null=True, blank=True)
    source_content = models.TextField("Текст статьи/сообщения ", null=True, blank=True)
    region = models.ForeignKey(Region, on_delete=models.DO_NOTHING, verbose_name="Регион")

    city_name = models.CharField("Город (населённый пункт)", max_length=100)

    company_name = models.CharField("Название организации", max_length=100, blank=False, null=True)
    groupOfRights = models.ForeignKey(GroupOfRights, on_delete=models.DO_NOTHING, verbose_name="Группа прав")


    tradeUnionRight = models.ForeignKey(TradeUnionRight, on_delete=models.DO_NOTHING,
                                        verbose_name="Нарушение в сфере профсоюзных прав и гражданских свобод")
    tradeUnionRightAnother = models.CharField("Другое", max_length=50, help_text='Введите значение', null=True,
                                              blank=True)
    tradeUnionCrime = models.ForeignKey(TradeUnionCrime, on_delete=models.DO_NOTHING,
                                        verbose_name="Обвинения в преступном поведении в связи с профсоюзной деятельностью")
    tradeUnionCrimeAnother = models.CharField("Другое", max_length=50, help_text='Введите значение', null=True,
                                              blank=True)


    # rightsViolation = models.ForeignKey(RightsViolation, on_delete=models.DO_NOTHING,
    #                                     verbose_name="Какое право нарушено")
    # rightsViolationAnother = models.CharField("Другое", max_length=50, help_text='Введите значение', null=True,
    #                                           blank=True)

    # rightsViolationCase = models.ForeignKey(RightsViolationCase, on_delete=models.DO_NOTHING,
    #                                         verbose_name="Обвинения в преступном поведении в связи с профсоюзной деятельностью",
    #                                         null=True)
    # rightsViolationCaseAnother = models.CharField("Другое", max_length=50, help_text='Введите значение', null=True,
    #                                               blank=True)
    meetingsRight = models.ForeignKey(MeetingsRight, on_delete=models.DO_NOTHING,
                                            verbose_name="Нарушения права на проведение собраний и демонстраций",
                                            null=True)
    meetingsRightAnother = models.CharField("Другое", max_length=50, help_text='Введите значение', null=True,
                                                  blank=True)
    tradeUnionBuildingsRight = models.ForeignKey(TradeUnionBuildingsRight, on_delete=models.DO_NOTHING,
                                            verbose_name="Защита профсоюзных помещений и имущества профсоюзов",
                                            null=True)
    tradeUnionBuildingsRightAnother = models.CharField("Другое", max_length=50, help_text='Введите значение', null=True,
                                                  blank=True)
    createOrganizationRight = models.ForeignKey(CreateOrganizationRight, on_delete=models.DO_NOTHING,
                                        verbose_name="Создание организации без предварительного разрешения")
    createOrganizationRightAnother = models.CharField("Другое", max_length=50, help_text='Введите значение', null=True,
                                              blank=True)
    createTradeUnionRight = models.ForeignKey(CreateTradeUnionRight, on_delete=models.DO_NOTHING,
                                        verbose_name="Создание профсоюзов и вступление в профсоюзы ")
    createTradeUnionRightAnother = models.CharField("Другое", max_length=50, help_text='Введите значение', null=True,
                                              blank=True)
    electionsRight = models.ForeignKey(ElectionsRight, on_delete=models.DO_NOTHING,
                                        verbose_name="Нарушение права свободно выбирать своих представителей")
    electionsRightAnother = models.CharField("Другое", max_length=50, help_text='Введите значение', null=True,
                                              blank=True)
    tradeUnionActivityRight = models.ForeignKey(TradeUnionActivityRight, on_delete=models.DO_NOTHING,
                                        verbose_name="Нарушения права профсоюза организовывать деятельность своего аппарата")
    tradeUnionActivityRightAnother = models.CharField("Другое", max_length=50, help_text='Введите значение', null=True,
                                              blank=True)
    createStrikeRight = models.ForeignKey(CreateStrikeRight, on_delete=models.DO_NOTHING,
                                        verbose_name="Нарушение права на забастовку")
    createStrikeRightAnother = models.CharField("Другое", max_length=50, help_text='Введите значение', null=True,
                                              blank=True)

    case_date = models.DateTimeField("Дата нарушения")

    group = models.ForeignKey(GroupOfPersons, on_delete=models.DO_NOTHING, verbose_name="Группа лиц", null=True)

    intruder = models.ForeignKey(Intruder, on_delete=models.DO_NOTHING, verbose_name="Нарушитель", null=False,
                                 default=None)
    agency_name = models.CharField("Название органа", max_length=500, null=True)
    company = models.ForeignKey(Company, on_delete=models.DO_NOTHING, verbose_name="Работодатель(компания)", null=True)
    intruder_another = models.CharField("Информация о нарушителе прав", max_length=500, null=True)
    description = models.CharField("Точные имена, даты, места событий", max_length=200, blank=False, null=True)
    full_description = models.CharField("Укажите ПОСЛЕДОВАТЕЛЬНО, что произошло", max_length=1800, blank=False, null=True),
    actions = models.CharField("Действия предприняты профсоюзом/правозащитной организацией", max_length=1800,
                               blank=False, null=True),
    result = models.CharField("Чем завершилась ситуация (если завершилась) или состояние в текущий момент",
                              max_length=1800, blank=False, null=True),

    violation_nature=models.ForeignKey(NatureViolation,on_delete=models.DO_NOTHING, verbose_name="Характер нарушения", null=True)
    rights_state=models.ForeignKey(RightsState,on_delete=models.DO_NOTHING, verbose_name="Ситуация с правами", null=True)
    rights_state_another=models.CharField("Другое", max_length=50, help_text='Введите значение', null=True,
                                              blank=False)
    victim_situation=models.ForeignKey(VictimSituation,on_delete=models.DO_NOTHING, verbose_name="Ситуация с потерпевшим(и)", null=True)
    victim_situation_another=models.CharField("Другое", max_length=50, help_text='Введите значение', null=True,
                                              blank=False)
    case_text = models.TextField("Кейсы, связанные с забастовкой", max_length=1800, null=True, blank=True)
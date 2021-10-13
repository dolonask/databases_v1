from django.conf import settings
from django.db import models


# Create your models here.


class Country(models.Model):
    name = models.CharField("Название", max_length=150)
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
    tradeunion_name = models.CharField("Укажите объединение (название федерации, конфедерации профсоюзов) "
                                       , max_length=500,
                                       null=True,blank=True)
    branch_name = models.CharField("Название отраслевой профсоюзной организации", max_length=500,
                                   null=True,blank=True)
    victim_name = models.CharField("Название организации, права которой были нарушены (федерация, отраслевое объединение, первичная организация) ", max_length=500,
                        )
    contacts = models.CharField("Контактные данные этой организации (электронная почта, адрес\телефон) ", max_length=500,
                                help_text='электронная почта, адрес\телефон')

    def __str__(self):
        return self.tradeunion_name

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
    is_anonim = models.CharField("Анонимно", choices=[('YES', 'Да'), ('NO', 'Нет'), ], max_length=20)
    name = models.CharField("ФИО", max_length=100, blank=True, null=True)
    member_of_tradeunion = models.CharField("Член профсоюза", choices=[('YES', 'Да'), ('NO', 'Нет'), ], max_length=20)
    gender = models.ForeignKey(Gender, on_delete=models.DO_NOTHING, verbose_name="Пол пострадавшего")
    age = models.CharField("Возраст пострадавшего", max_length=50,)
    education = models.ForeignKey(Education, on_delete=models.DO_NOTHING, verbose_name="Образование")
    marital_status = models.ForeignKey(MaritalStatus, on_delete=models.DO_NOTHING, verbose_name="Состояние в браке")
    position = models.CharField("Должность в организации", max_length=50, )
    experience = models.CharField("Стаж работы в организации", max_length=50,)
    is_official = models.CharField("Было ли официальное трудоустройство?", choices=[('YES', 'Да'), ('NO', 'Нет')],
                                   max_length=20, null=True, blank=True)
    has_agreement = models.CharField("Был ли подписан трудовой договор?", choices=[('YES', 'Да'), ('NO', 'Нет')],
                                     max_length=20, blank=True, null=True)
    agreementDetail = models.ForeignKey(AgreementDetail, on_delete=models.DO_NOTHING, verbose_name="Детали договора", null=True, blank=True)
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
    type_another = models.CharField("Другое", max_length=50, null=True,blank=True)
    membership = models.ForeignKey(MembershipOfGroupPersons, on_delete=models.DO_NOTHING,
                                   verbose_name="Членство в профсоюзе ")
    membership_another = models.CharField("Другое", max_length=50, null=True,blank=True)

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

    name = models.CharField("Выбор", max_length=255)
    active = models.BooleanField("Активен", default=True)

    def __str__(self):
        return self.name

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
    company_name = models.CharField("Название организации (с указанием организационно-правовой формы)", max_length=100,
                                    help_text='Название')
    address = models.CharField("Адрес / Телефон", max_length=100, help_text='Адрес')
    product_type = models.CharField("Вид производимой продукции / Предоставляемые услуги ", max_length=100,
                                    help_text='Вид производимой продукции / Предоставляемые услуги ')
    ownership = models.ForeignKey(OwnerShipType, on_delete=models.DO_NOTHING,
                                  verbose_name="Форма собственности компании")
    country_from = models.CharField("Страна происхождения компании", max_length=100,
                                    help_text='Страна происхождения кампании')
    is_tnk_member = models.CharField("Является ли эта кампания частью ТНК (Транснациональная компания)",
                                     choices=[('YES', 'Да'), ('NO', 'Нет'), ], max_length=20, null=True,
                                     blank=True)
    tnk_name = models.CharField("Название ТНК, в которую входит эта компания", max_length=100,
                                help_text='Название ТНК, в которую входит эта компания')
    company_experience = models.CharField("Время на рынке", max_length=100, help_text='Время на рынке ')
    branch = models.CharField("Отрасль деятельности", max_length=100, help_text='Отрасль деятельности')
    emp_count = models.ForeignKey(EmployeesCount, on_delete=models.DO_NOTHING, verbose_name="Численность работников")
    additional = models.CharField("Иная важная информация (Другие компании, связанные с ней, головная компания, подрядчики, поставщики и пр.)", max_length=2000)

    def __str__(self):
        return self.company_name

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


class AntiTradeUnionDiscrimination(models.Model):
    name = models.CharField("Название", max_length=255)
    active = models.BooleanField("Активен", default=True)

    def __str__(self):
        return self.name


class СonversationRight(models.Model):
    name = models.CharField("Название", max_length=255)
    active = models.BooleanField("Активен", default=True)

    def __str__(self):
        return self.name


class Сonvention135(models.Model):
    name = models.CharField("Название", max_length=255)
    active = models.BooleanField("Активен", default=True)

    def __str__(self):
        return self.name


class ConsultationRight(models.Model):
    name = models.CharField("Название", max_length=255)
    active = models.BooleanField("Активен", default=True)

    def __str__(self):
        return self.name


class DiscriminatiOnVariousGrounds(models.Model):
    name = models.CharField("Название", max_length=255)
    active = models.BooleanField("Активен", default=True)

    def __str__(self):
        return self.name


class PrincipleOfNonDiscrimination(models.Model):
    name = models.CharField("Название", max_length=255)
    active = models.BooleanField("Активен", default=True)

    def __str__(self):
        return self.name


class DiscriminationInVariousAreas(models.Model):
    name = models.CharField("Название", max_length=255)
    active = models.BooleanField("Активен", default=True)

    def __str__(self):
        return self.name


class PublicPolicyDiscrimination(models.Model):
    name = models.CharField("Название", max_length=255)
    active = models.BooleanField("Активен", default=True)

    def __str__(self):
        return self.name


class ChildLabor(models.Model):
    name = models.CharField("Название", max_length=255)
    active = models.BooleanField("Активен", default=True)

    def __str__(self):
        return self.name


class Сonvention138(models.Model):
    name = models.CharField("Название", max_length=255)
    active = models.BooleanField("Активен", default=True)

    def __str__(self):
        return self.name


class Сonvention87(models.Model):
    name = models.CharField("Название", max_length=255)
    active = models.BooleanField("Активен", default=True)

    def __str__(self):
        return self.name


class Сonvention98(models.Model):
    name = models.CharField("Название", max_length=255)
    active = models.BooleanField("Активен", default=True)

    def __str__(self):
        return self.name


class Сonvention182(models.Model):
    name = models.CharField("Название", max_length=255)
    active = models.BooleanField("Активен", default=True)

    def __str__(self):
        return self.name


class ProhibitionOfForcedLabor(models.Model):
    name = models.CharField("Название", max_length=255)
    active = models.BooleanField("Активен", default=True)

    def __str__(self):
        return self.name


class UseOfForcedLabor(models.Model):
    name = models.CharField("Название", max_length=255)
    active = models.BooleanField("Активен", default=True)

    def __str__(self):
        return self.name


class GovernmentCoercion(models.Model):
    name = models.CharField("Название", max_length=255)
    active = models.BooleanField("Активен", default=True)

    def __str__(self):
        return self.name


class ViolationsUsingCompulsoryLabor(models.Model):
    name = models.CharField("Название", max_length=255)
    active = models.BooleanField("Активен", default=True)

    def __str__(self):
        return self.name


class FailureSystemicMeasures(models.Model):
    name = models.CharField("Название", max_length=255)
    active = models.BooleanField("Активен", default=True)

    def __str__(self):
        return self.name


def files_location(instance, filename):
    return "%s/%s/%s" % ("files/work", instance.card.pk, filename)


def photos_location(instance, filename):
    return "%s/%s/%s" % ("photos/work", instance.card.pk, filename)


class CasePhoto(models.Model):
    photo = models.FileField("Фото/видео/документы", upload_to="document/%Y/%m/%d/", null=True)
    card = models.ForeignKey("Case", on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.photo

    class Meta:
        verbose_name = "Фото/видео/документы "
        verbose_name_plural = "Фото/видео/документы "


class CaseFile(models.Model):
    file = models.FileField("Кейсы, связанные с данной ситуацией", upload_to=files_location, null=True)
    card = models.ForeignKey("Case", on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.file

    class Meta:
        verbose_name = "Кейсы, связанные с данной ситуацией"
        verbose_name_plural = "Кейсы, связанные с данной ситуацией"


#
# class UserCountry(models.Model):
#     user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING, null=True,
#                                  verbose_name="Монитор")
#     country = models.ForeignKey(Country, on_delete=models.DO_NOTHING, verbose_name="Страна")
#
#     def __str__(self):
#         return self.user.name + self.country.name
#
#     class Meta:
#         verbose_name = "Страна пользователя"
#         verbose_name_plural = "Страны пользователя"


class Case(models.Model):
    case_name = models.CharField("Название (описание) карточки", max_length=50,
                                 help_text='Название (описание) карточки')
    date_create = models.DateTimeField("Дата создания", auto_now_add=True)
    date_update = models.DateTimeField("Дата последних изменений", auto_now=True)
    source = models.ManyToManyField(Source, verbose_name="Источник информации о нарушении")
    source_another = models.CharField("Другое", max_length=50, null=True, blank=True)
    source_url = models.CharField("Источник информации", max_length=255, null=True, blank=True)
    source_content = models.TextField("Текст статьи/сообщения", null=True, blank=True)
    country = models.ForeignKey(Country, on_delete=models.DO_NOTHING, verbose_name="Страна")
    region = models.ForeignKey(Region, on_delete=models.DO_NOTHING, verbose_name="Регион")

    city_name = models.CharField("Город (населённый пункт)", max_length=100)

    case_company_name = models.CharField("Название организации", max_length=100, blank=True, null=True)
    groupOfRights = models.ForeignKey(GroupOfRights, on_delete=models.DO_NOTHING, verbose_name="Группа прав")

    tradeUnionRight = models.ForeignKey(TradeUnionRight, on_delete=models.DO_NOTHING,
                                        verbose_name="Нарушение в сфере профсоюзных прав и гражданских свобод", null=True, blank=True)
    tradeUnionRightAnother = models.CharField("Другое", max_length=50, help_text='Введите значение', null=True,
                                              blank=True)
    tradeUnionCrime = models.ForeignKey(TradeUnionCrime, on_delete=models.DO_NOTHING,
                                        verbose_name="Обвинения в преступном поведении в связи с профсоюзной деятельностью",
                                        null=True, blank=True)
    tradeUnionCrimeAnother = models.CharField("Другое", max_length=50, help_text='Введите значение',
                                              null=True, blank=True)

    meetingsRight = models.ForeignKey(MeetingsRight, on_delete=models.DO_NOTHING,
                                      verbose_name="Нарушения права на проведение собраний и демонстраций",
                                      null=True, blank=True)
    meetingsRightAnother = models.CharField("Другое", max_length=50, help_text='Введите значение', null=True,
                                            blank=True)

    сonvention87 = models.ForeignKey(Сonvention87, on_delete=models.DO_NOTHING,
                                     verbose_name="Нарушения положений Конвенции МОТ №87", null=True, blank=True)

    tradeUnionBuildingsRight = models.ForeignKey(TradeUnionBuildingsRight, on_delete=models.DO_NOTHING,
                                                 verbose_name="Защита профсоюзных помещений и имущества профсоюзов",blank=True,
                                                 null=True)
    tradeUnionBuildingsRightAnother = models.CharField("Другое", max_length=50, help_text='Введите значение', null=True,
                                                       blank=True)
    createOrganizationRight = models.ForeignKey(CreateOrganizationRight, on_delete=models.DO_NOTHING,
                                                verbose_name="Создание организации без предварительного разрешения",null=True, blank=True)
    createOrganizationRightAnother = models.CharField("Другое", max_length=50, help_text='Введите значение', null=True,
                                                      blank=True)
    createTradeUnionRight = models.ForeignKey(CreateTradeUnionRight, on_delete=models.DO_NOTHING,
                                              verbose_name="Создание профсоюзов и вступление в профсоюзы"
                                              , null=True, blank=True)
    createTradeUnionRightAnother = models.CharField("Другое", max_length=50, help_text='Введите значение', null=True,
                                                    blank=True)
    electionsRight = models.ForeignKey(ElectionsRight, on_delete=models.DO_NOTHING,
                                       verbose_name="Нарушение права свободно выбирать своих представителей"
                                       , null=True, blank=True)
    electionsRightAnother = models.CharField("Другое", max_length=50, help_text='Введите значение', null=True,
                                             blank=True)
    tradeUnionActivityRight = models.ForeignKey(TradeUnionActivityRight, on_delete=models.DO_NOTHING,
                                                verbose_name="Нарушения права профсоюза организовывать деятельность своего аппарата"
                                                , null=True, blank=True)
    tradeUnionActivityRightAnother = models.CharField("Другое", max_length=50, help_text='Введите значение', null=True,
                                                      blank=True)
    createStrikeRight = models.ForeignKey(CreateStrikeRight, on_delete=models.DO_NOTHING,
                                          verbose_name="Нарушение права на забастовку"
                                          , null=True, blank=True)
    createStrikeRightAnother = models.CharField("Другое", max_length=50, help_text='Введите значение', null=True,
                                                blank=True)

    сonvention98 = models.ForeignKey(Сonvention98, on_delete=models.DO_NOTHING,
                                     verbose_name="Нарушения положений Конвенции МОТ №98", null=True, blank=True)

    antiTradeUnionDiscrimination = models.ForeignKey(AntiTradeUnionDiscrimination, on_delete=models.DO_NOTHING,
                                                     verbose_name="Антипрофсоюзная дискриминация", null=True, blank=True)
    antiTradeUnionDiscriminationAnother = models.CharField("Другое", max_length=50, help_text='Введите значение',
                                                           null=True,
                                                           blank=True)
    conversationRight = models.ForeignKey(СonversationRight, on_delete=models.DO_NOTHING,
                                          verbose_name="Нарушения права на проведение коллективных переговоров"
                                          , null=True, blank=True)
    conversationRightAnother = models.CharField("Другое", max_length=50, help_text='Введите значение',
                                                null=True,
                                                blank=True)
    сonvention135 = models.ForeignKey(Сonvention135, on_delete=models.DO_NOTHING,
                                      verbose_name="Нарушения положений Конвенции МОТ №135"
                                      , null=True, blank=True)
    сonvention135Another = models.CharField("Другое", max_length=50, help_text='Введите значение',
                                            null=True,
                                            blank=True)
    consultationRight = models.ForeignKey(ConsultationRight, on_delete=models.DO_NOTHING,
                                          verbose_name="Проведение консультаций", null=True, blank=True)
    consultationRightAnother = models.CharField("Другое", max_length=50, help_text='Введите значение',
                                                null=True,
                                                blank=True)
    principleOfNonDiscrimination = models.ForeignKey(PrincipleOfNonDiscrimination, on_delete=models.DO_NOTHING,
                                                     verbose_name="Принцип запрещения дискриминации", null=True,
                                                     blank=True)
    discriminatiOnVariousGrounds = models.ForeignKey(DiscriminatiOnVariousGrounds, on_delete=models.DO_NOTHING,
                                                     verbose_name="Дискриминация по различным основаниям", null=True,
                                                     blank=True)

    discriminationInVariousAreas = models.ForeignKey(DiscriminationInVariousAreas, on_delete=models.DO_NOTHING,
                                                     verbose_name="Дискриминация в различных сферах трудовых отношений",
                                                     null=True, blank=True)
    discriminationInVariousAreasAnother = models.CharField("Другое", max_length=50, help_text='Введите значение',
                                                           null=True,
                                                           blank=True)
    publicPolicyDiscrimination = models.ForeignKey(PublicPolicyDiscrimination, on_delete=models.DO_NOTHING,
                                                   verbose_name="Нарушения в области проведения государственной политики "
                                                                "по искоренению дискриминации и поощрению равенства прав и возможностей",
                                                   null=True, blank=True)
    childLabor = models.ForeignKey(ChildLabor, on_delete=models.DO_NOTHING,
                                   verbose_name="Использование детского труда",
                                   null=True, blank=True)

    сonvention138 = models.ForeignKey(Сonvention138, on_delete=models.DO_NOTHING,
                                      verbose_name="О минимальном возрасте для приема на работу",
                                      null=True, blank=True)
    convention182 = models.ForeignKey(Сonvention182, on_delete=models.DO_NOTHING,
                                      verbose_name="О запрещении и немедленных мерах по искоренению наихудших форм детского труда",
                                      null=True, blank=True)

    prohibitionOfForcedLabor = models.ForeignKey(ProhibitionOfForcedLabor, on_delete=models.DO_NOTHING,
                                                 verbose_name="Запрет принудительного труда",
                                                 null=True, blank=True)
    useOfForcedLabor = models.ForeignKey(UseOfForcedLabor, on_delete=models.DO_NOTHING,
                                         verbose_name="Использование принудительного труда",
                                         null=True, blank=True)
    governmentCoercion = models.ForeignKey(GovernmentCoercion, on_delete=models.DO_NOTHING,
                                           verbose_name="Косвенное принуждение государством к труду",
                                           null=True, blank=True)
    violationsUsingCompulsoryLabor = models.ForeignKey(ViolationsUsingCompulsoryLabor, on_delete=models.DO_NOTHING,
                                                       verbose_name="Нарушения при использовании принудительного (обязательного) труда в допустимых случаях",
                                                       null=True, blank=True)

    failureSystemicMeasures = models.ForeignKey(FailureSystemicMeasures, on_delete=models.DO_NOTHING,
                                                verbose_name="Нарушения, связанные с непринятием государством системных мер",
                                                null=True, blank=True)

    start_date = models.DateTimeField("Дата начала")
    end_date = models.DateTimeField("Дата завершения", null=True, blank=True)
    INTERVAL_OR_EXACT = [
        (0, 'Точная'),
        (1, 'Интервал')
    ]
    date_type = models.BooleanField("Тип даты нарушения", choices=INTERVAL_OR_EXACT, default=0)
    victim = models.ForeignKey(Victim, on_delete=models.DO_NOTHING,
                               verbose_name="В отношении кого совершено нарушение:", null=True, blank=True)
    tradeUnionInfo = models.ForeignKey(TradeUnionInfo, on_delete=models.DO_NOTHING,
                                       verbose_name="Профсоюзная организация", null=True, blank=True)
    # individualInfo = models.ForeignKey(IndividualInfo, on_delete=models.DO_NOTHING, verbose_name="Физическое лицо", null=True, blank=True)
    groupOfPersons = models.ForeignKey(GroupOfPersons, on_delete=models.DO_NOTHING,
                                       verbose_name="Группа лиц (работников)", null=True, blank=True)

    intruder = models.ManyToManyField(Intruder, verbose_name="Кем было совершено нарушение", null=False)
    intruderAnother = models.CharField("Другое", max_length=50, help_text='Введите значение',
                                       null=True,
                                       blank=True)
    government_agency_name = models.CharField("Название государственного органа, полное с указанием территориальной принадлежности ", max_length=200, null=True, blank=True)
    local_agency_name = models.CharField("Название органа местного самоуправления, полное с указанием территориальной принадлежности ", max_length=500, null=True,
                                         blank=True)
    police_agency_name = models.CharField("Название правоохранительного органа, полное с указанием территориальной принадлежности ", max_length=500, null=True, blank=True)
    # control_agency_name = models.CharField("Название контролирующего органа", max_length=500, null=True, blank=True)
    company = models.ForeignKey(Company, on_delete=models.DO_NOTHING, verbose_name="Работодатель(компания)", null=True, blank=True)

    exact_data = models.TextField("Укажите точные имена, даты, места событий", blank=True, null=True, max_length=1000)
    case_description = models.TextField("Укажите ПОСЛЕДОВАТЕЛЬНО, что произошло. "
                                        "Параллельно указывайте, чем подтверждаются эти факты "
                                        "(если есть приложения, укажите сразу номера и названия соответствующих приложений)",
        max_length=1800, blank=True, null=True)
    tradeunion_actions = models.TextField("Опишите, какие действия предприняты профсоюзом/правозащитной организацией."
                                          " Параллельно указывайте, чем подтверждаются эти факты (если есть приложения,"
                                          " укажите сразу номера и названия соответствующих приложений)",
        max_length=2000, blank=True, null=True)
    case_result = models.TextField("Чем завершилась ситуация (если завершилась) или состояние в текущий момент", max_length=2000, blank=True, null=True)

    violation_nature = models.ForeignKey(NatureViolation, on_delete=models.DO_NOTHING,
                                         verbose_name="Характер нарушения", null=True, blank=True)
    rights_state = models.ForeignKey(RightsState, on_delete=models.DO_NOTHING, verbose_name="Ситуация с правами",
                                     null=True, blank=True)
    rights_state_another = models.CharField("Другое", max_length=50, help_text='Введите значение', null=True,
                                            blank=True)
    victim_situation = models.ForeignKey(VictimSituation, on_delete=models.DO_NOTHING,
                                         verbose_name="Ситуация с потерпевшим(и)", null=True, blank=True)
    victim_situation_another = models.CharField("Другое", max_length=50, help_text='Введите значение', null=True,
                                                blank=True)
    tradeUnionSituation = models.ForeignKey(TradeUnionSituation, on_delete=models.DO_NOTHING,
                                            verbose_name="Профсоюз на месте работы после произошедшего",
                                            null=True, blank=True)
    tradeUnionSituation_another = models.CharField("Другое", max_length=50, help_text='Введите значение', null=True,
                                                   blank=True)
    tradeUnionCount = models.ForeignKey(TradeUnionCount, on_delete=models.DO_NOTHING,
                                        verbose_name="Численность профсоюза после произошедшего",
                                        null=True, blank=True)

    case_text = models.TextField("Кейсы, связанные с данной ситуацией", max_length=1800, null=True, blank=True)
    trade_union_activities = models.ForeignKey('TradeUnionActivities', on_delete=models.DO_NOTHING,
                                               verbose_name='Отрасль деятельности профсоюза', null=True, blank=True)
    trade_union_activities_another = models.CharField('Отрасль деятельности профсоюза(Другое)', max_length=50, null=True, blank=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING, null=True,
                             verbose_name="Монитор", related_name="strike_users", blank=True)
    active = models.BooleanField("Активен", default=True)
    comment = models.TextField('Комментарии для монитора', max_length=500, blank=True, null=True)

    class Meta:
        verbose_name = 'Кейс трудовые нарушения'
        verbose_name_plural = 'Кейсы трудовых нарушений'


class CaseComment(models.Model):
    comment = models.TextField("Коментрий")
    active = models.BooleanField("Активен", default=True)
    date_create = models.DateTimeField("Дата создания", auto_now_add=True)
    case = models.ForeignKey(Case, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Коментарий к трудовому нарушению"
        verbose_name_plural = "Коментарии к трудовым нарушениям"


class TradeUnionActivities(models.Model):
    name = models.CharField('Название', max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Отрасль деятельности профсоюза"
        verbose_name_plural = "Отрасли деятельности профсоюзов"

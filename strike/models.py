from datetime import datetime

from django.conf import settings
from django.db import models


# Create your models here.

class TradeUnion(models.Model):
    name = models.CharField("Значение", max_length=100, blank=False)
    visible = models.BooleanField("Видимый", default=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Есть ли на предприятии профсоюз"
        verbose_name = "Есть ли на предприятии профсоюзы"


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


class ParticipantsCount(models.Model):
    choice = models.CharField("Выбор", max_length=255)
    active = models.BooleanField("Активен", default=True)

    def __str__(self):
        return self.choice

    class Meta:
        verbose_name = "Количество участников забастовки"
        verbose_name_plural = "Количество участников забастовки"




class DemandCategory(models.Model):
    demand_cat_name = models.CharField("Название", max_length=255)
    # demand_type = models.ForeignKey('DemandType', on_delete=models.DO_NOTHING, null=True, blank=True,
    #                                 verbose_name='Тип требования')
    active = models.BooleanField("Активен", default=True)

    def __str__(self):
        return self.demand_cat_name

    class Meta:
        verbose_name = "Характер требования"
        verbose_name_plural = "Характеры требований"


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


class Source(models.Model):
    name = models.CharField("Название", max_length=100, help_text='Название источника')
    active = models.BooleanField("Активен", default=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Источник"
        verbose_name_plural = "Источники"


class GroupCharacter(models.Model):
    name = models.CharField("Значение", max_length=100)
    active = models.BooleanField("Активен", default=True)

    class Meta:
        verbose_name = "Характер групп"
        verbose_name_plural = "Характеры групп"

    def __str__(self):
        return self.name


class TradeUnionGroupMembership(models.Model):
    name = models.CharField("Значение", max_length=100)
    active = models.BooleanField("Активен", default=True)

    class Meta:
        verbose_name = "Членство в профсоюзе"
        verbose_name_plural = "Членства в профсоюзе"

    def __str__(self):
        return self.name


class PersonGroupInfo(models.Model):
    groupCharacter = models.ForeignKey(GroupCharacter, on_delete=models.DO_NOTHING, verbose_name="Характер группы")
    groupCharacter_another = models.CharField("Другое", max_length=50, help_text='Введите значение', null=True,
                                              blank=True)
    tradeUnionMembership = models.ForeignKey(TradeUnionGroupMembership, on_delete=models.DO_NOTHING,
                                             verbose_name="Членство в профсоюзе")

    class Meta:
        verbose_name = "Группа лиц"
        verbose_name_plural = "Группы лиц"

    def __str__(self):
        return self.name


class TradeunionData(models.Model):
    tradeUnion_name = models.CharField("Название", max_length=100, help_text='Название профсоюза')
    tradeUnion_contacts = models.CharField("Реквизиты (контакты/адрес и т.д.) ", max_length=200,
                                           help_text='Реквизиты (контакты/адрес и т.д.)')

    class Meta:
        verbose_name = "Профсоюз"
        verbose_name_plural = "Профсоюзы"


class Employer(models.Model):
    emp_name = models.CharField("Название", max_length=100, help_text='Название')
    emp_contacts = models.CharField("Реквизиты (контакты/адрес и т.д.) ", max_length=200,
                                    help_text='Реквизиты (контакты/адрес и т.д.) ')

    class Meta:
        verbose_name = "Работодатель"
        verbose_name_plural = "Работодатели"


class Age(models.Model):
    name = models.CharField("Возраст", max_length=100)
    active = models.BooleanField("Активен", default=True)

    class Meta:
        verbose_name = "Возраст"
        verbose_name_plural = "Возраст"

    def __str__(self):
        return self.name


class Individual(models.Model):
    genders = [
        ("MALE", "Мужской"),
        ("FEMALE", "Женский")
    ]
    is_anonim = models.CharField("Анонимно", choices=[('YES', 'Да'), ('NO', 'Нет'), ], max_length=20)
    individual_name = models.CharField("ФИО", max_length=150)
    gender = models.CharField("Пол", choices=genders, max_length=20)
    age = models.ForeignKey(Age, on_delete=models.DO_NOTHING, verbose_name="Возраст")
    profession = models.CharField("Профессия", max_length=100,)
    card = models.ForeignKey("Card", on_delete=models.DO_NOTHING)

    class Meta:
        verbose_name = "Физическое лицо"
        verbose_name_plural = "Физические лица"


class Initiator(models.Model):
    name = models.CharField("ФИО", max_length=150, help_text='ФИО')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Инициатор забастовки/акции"
        verbose_name_plural = "Инициаторы забастовки/акции"


def files_location(instance, filename):
    return "%s/%s/%s" % ("files/strike", instance.card.pk, filename)


def photos_location(instance, filename):
    return "%s/%s/%s" % ("photos/strike", instance.card.pk, filename)


class CardPhoto(models.Model):
    photo = models.FileField("Фото/видео/документы", upload_to=photos_location)
    card = models.ForeignKey("Card", on_delete=models.DO_NOTHING, null=True)

    def __str__(self):
        return self.photo.path

    class Meta:
        verbose_name = "Фото/видео/документы "
        verbose_name_plural = "Фото/видео/документы "


class CardFile(models.Model):
    file = models.FileField("Кейсы, связанные с забастовкой", upload_to=files_location)
    card = models.ForeignKey("Card", on_delete=models.DO_NOTHING, null=True)

    def __str__(self):
        return self.file

    class Meta:
        verbose_name = "Кейсы, связанные с забастовкой"
        verbose_name_plural = "Кейсы, связанные с забастовкой"


class TradeunionChoice(models.Model):
    name = models.CharField("Значение", max_length=100)
    active = models.BooleanField("Активен", default=True)

    class Meta:
        verbose_name = "Есть ли на предприятии профсоюз"
        verbose_name_plural = "Есть ли на предприятии профсоюзы"

    def __str__(self):
        return self.name


class StrikeCharacter(models.Model):
    name = models.CharField("Значение", max_length=100)
    active = models.BooleanField("Активен", default=True)

    class Meta:
        verbose_name = "Характер забастовки/акции"
        verbose_name_plural = "Характеры забастовки/акции"

    def __str__(self):
        return self.name

class EconomicDemand(models.Model):
    name = models.CharField("Значение", max_length=100)
    active = models.BooleanField("Активен", default=True)

    class Meta:
        verbose_name = "Экономический"
        verbose_name_plural = "Экономические"

    def __str__(self):
        return self.name

class PoliticDemand(models.Model):
    name = models.CharField("Значение", max_length=100)
    active = models.BooleanField("Активен", default=True)

    class Meta:
        verbose_name = "Политический"
        verbose_name_plural = "Политический"

    def __str__(self):
        return self.name

class ComboDemand(models.Model):
    name = models.CharField("Значение", max_length=100)
    active = models.BooleanField("Активен", default=True)

    class Meta:
        verbose_name = "Смешанный"
        verbose_name_plural = "Смешанный"

    def __str__(self):
        return self.name


class MeetingRequirment(models.Model):
    name = models.CharField("Значение", max_length=100)
    active = models.BooleanField("Активен", default=True)

    class Meta:
        verbose_name = "Удовлетворение требований "
        verbose_name_plural = "Удовлетворения требований"

    def __str__(self):
        return self.name


class Card(models.Model):
    id = models.BigAutoField("№", primary_key=True)
    name = models.CharField("Название", max_length=100, blank=False)
    card_sources = models.ManyToManyField(Source, verbose_name="Источник")
    source_url = models.CharField("Источник информации (ссылка)", max_length=255, null=True, blank=True)
    source_content = models.TextField("Текст статьи/сообщения ", null=True, blank=True)
    country = models.ForeignKey(Country, on_delete=models.DO_NOTHING, verbose_name="Страна")
    region = models.ForeignKey(Region, on_delete=models.DO_NOTHING, verbose_name="Регион")
    city_name = models.CharField("Название города", max_length=100, null=True, blank=False)

    company_name = models.CharField("Название предприятия (юридического лица)", max_length=100, blank=False)

    company_ownership_type = models.ForeignKey(OwnerShipType, on_delete=models.DO_NOTHING, null=True, blank=True,
                                               verbose_name="Форма собственности компании", )

    company_country_name = models.CharField("Страна происхождения компании", max_length=100, blank=True)

    company_is_tnk_member = models.CharField("Является ли эта кампания частью ТНК (Транснациональная компания)",
                                             choices=[('YES', 'Да'), ('NO', 'Нет'), ], max_length=20, null=True, blank=True)

    company_tnk_name = models.CharField("Название ТНК (Транснациональная компания), в которую входит эта кампания", max_length=100, null=True,
                                        blank=True)
    company_employees_count = models.ForeignKey(EmployeesCount, on_delete=models.DO_NOTHING,
                                                verbose_name='Общая численность работников на предприятии')

    count_strike_participants = models.ForeignKey(ParticipantsCount, on_delete=models.DO_NOTHING,
                                                  verbose_name="Количество участников забастовки/акции")
    card_demand_categories = models.ManyToManyField(DemandCategory, verbose_name="Характер требований", null=True, blank=True)
    economic_demands = models.ManyToManyField(EconomicDemand, verbose_name="Экономический", null=True, blank=True)
    economic_another = models.CharField("Другое", max_length=50, help_text='Введите значение', null=True, blank=True)
    politic_demands = models.ManyToManyField(PoliticDemand, verbose_name="Политический", null=True, blank=True)

    politic_another = models.CharField("Другое", max_length=50, help_text='Введите значение', null=True, blank=True)
    combo_demands = models.ManyToManyField(ComboDemand, verbose_name="Смешанный", null=True, blank=True)
    combo_another = models.CharField("Другое", max_length=50, help_text='Введите значение', null=True, blank=True)

    start_date = models.DateTimeField("Дата начало проведения забастовки/акции")
    end_date = models.DateTimeField("Дата конца проведения забастовки/акции", null = True, blank=True)
    tradeunionChoice = models.ForeignKey(TradeunionChoice, on_delete=models.DO_NOTHING,
                                         verbose_name="Есть ли на предприятии профсоюз")
    tradeunionChoiceAnother = models.CharField("Другое", max_length=50, help_text='Введите значение', null=True,
                                               blank=True)

    date_create = models.DateTimeField("Дата создания", auto_now_add=True)
    date_update = models.DateTimeField("Дата последних изменений", auto_now=True)
    active = models.BooleanField("Активен", default=True)
    comment = models.TextField('Комментарии для монитора', max_length=500, blank=True, null=True)

    THE_NATURE_OF_THE_GROUP = [
        ('Б/ПГ', 'Бригада или производственная группа'),
        ('опр категория', 'Определенная категория работников'),
        ('Др', 'Другое'),
    ]

    TRADE_UNION_MEMBERSHIP = [
        ('Все', 'Все состоят в профсоюзе'),
        ('Не все', 'В профсоюзе состоят не все'),
        ('Никто', 'Никто не состоит в профсоюзе'),
    ]

    GENDER = [
        ('М', 'Мужчина'),
        ('Ж', 'Женщина'),
    ]

    AGE = [
        ('<18', 'менее 18 лет'),
        ('19-62', '19-62'),
        ('> 63', '63 и старше'),
    ]

    added_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING, null=True,
                                 verbose_name="Монитор")
    initiator = models.ForeignKey(Initiator, on_delete=models.DO_NOTHING, verbose_name="Инициатор забастовки/акции",
                                  null=True)
    tradeunion_data = models.ForeignKey(TradeunionData, on_delete=models.DO_NOTHING, verbose_name="Данные профсоюза",
                                        null=True, blank=True)
    personGroupInfo = models.ForeignKey(PersonGroupInfo, on_delete=models.DO_NOTHING, verbose_name="Группа лиц",
                                        null=True, blank=True)

    employear = models.ForeignKey(Employer, on_delete=models.DO_NOTHING, verbose_name="Работодатель", null=True,
                                  blank=True)

    DURATIONS = [
        ('LONG', 'Кратковременная'),
        ('SHORT', 'Длящаяся')
    ]
    RESULTS = [
        ('+', 'удовлетворены'),
        ('-', 'не удовлетворены'),
        ('+-', 'удовлетворены частично')
    ]
    duration = models.ForeignKey(StrikeCharacter, on_delete=models.DO_NOTHING,
                                 verbose_name='Характер забастовки/акции - сколько длилась', null=True)
    meeting_requirements = models.ForeignKey(MeetingRequirment, on_delete=models.DO_NOTHING,
                                             verbose_name='Удовлетворение требований', null=True)

    story = models.TextField('Укажите ПОСЛЕДОВАТЕЛЬНО, что произошло. Параллельно указывайте, чем подтверждаются эти факты (если есть приложения, укажите сразу номера и названия соответствующих приложений) ',max_length=1800)
    reasons_for_strike = models.TextField('Опишите причины начала забастовки (например: условия труда на предприятии, продолжительность рабочего времени, безопасность и т.д. время, связанное с работой)',max_length=1800)
    change_number_participants = models.TextField('Опишите как менялось количество участников забастовки во время проведения и что на это влияло?', max_length=1800)
    initiators_and_participants = models.TextField('Ситуация с инициаторами и участниками забастовки/акции (продолжают ли они работать, применялись ли к ним административные меры со стороны предприятия). ', max_length=1800)
    state_position = models.TextField("Позиция государства (Опишите реакцию государственных органов)", max_length=1800)
    results_so_far = models.TextField('Опишите, с какими итогами закончилась забастовка, если еще не закончилась, то какие итоги на данный момент.', max_length=1800)
    additional_information = models.TextField("Любая дополнительная информация", null=True, blank=True)

    case_text = models.TextField("Окно для внесения информации", max_length=1800, null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Карточка"
        verbose_name_plural = "Карточки"

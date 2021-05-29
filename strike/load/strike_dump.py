
def load_strikes(apps,schema_editor):

    print("MeetingRequirment")
    MeetingRequirment = apps.get_model("strike", "MeetingRequirment")
    meetingRequirment = MeetingRequirment(id=1, name='удовлетворены', active=True)
    meetingRequirment.save()
    meetingRequirment = MeetingRequirment(id=2, name='не удовлетворены', active=True)
    meetingRequirment.save()
    meetingRequirment = MeetingRequirment(id=3, name='удовлетворены частично', active=True)
    meetingRequirment.save()

    print("StrikeCharacter")
    StrikeCharacter = apps.get_model("strike", "StrikeCharacter")
    strikeCharacter = StrikeCharacter(id = 1, name='кратковременная', active = True)
    strikeCharacter.save()
    strikeCharacter = StrikeCharacter(id = 2, name='длящаяся', active = True)
    strikeCharacter.save()

    print("source")
    Source = apps.get_model("strike", "Source")
    source = Source(id = 1, name='СМИ/Блогер/Лидер мнения', active = True)
    source.save()
    source = Source(id = 2, name='Работники/участники протеста', active = True)
    source.save()
    source = Source(id = 3, name='Профсоюз', active = True)
    source.save()
    source = Source(id = 4, name='Представитель коллектива', active = True)
    source.save()
    source = Source(id = 5, name='Государственные органы', active = True)
    source.save()
    source = Source(id = 6, name='Не правительственные организации /гражданские активисты', active = True)
    source.save()
    print("Country")
    Country = apps.get_model("strike", "Country")
    country = Country(id=1, name='Россия', active=True)
    country.save()
    Region = apps.get_model("strike", "Region")

    region = Region(id=1, name='г.Москва', active=True, country=country)
    region.save()

    region = Region(id=2, name='Амурскаяобласть(Благовещенск)', active=True, country=country)
    region.save()

    region = Region(id=3, name='Архангельскаяобласть(Архангельск)', active=True, country=country)
    region.save()

    region = Region(id=4, name='Астраханскаяобласть(Астрахань)', active=True, country=country)
    region.save()

    region = Region(id=5, name='Белгородскаяобласть(Белгород)', active=True, country=country)
    region.save()

    region = Region(id=6, name='Брянскаяобласть(Брянск)', active=True, country=country)
    region.save()

    region = Region(id=7, name='Челябинскаяобласть(Челябинск)', active=True, country=country)
    region.save()

    region = Region(id=8, name='Иркутскаяобласть(Иркутск)', active=True, country=country)
    region.save()

    region = Region(id=9, name='Ивановскаяобласть(Иваново)', active=True, country=country)
    region.save()

    region = Region(id=10, name='Калининградскаяобласть(Калининград)', active=True, country=country)
    region.save()

    region = Region(id=11, name='Калужскаяобласть(Калуга)', active=True, country=country)
    region.save()

    region = Region(id=12, name='Кемеровскаяобласть—Кузбасс(Кемерово)', active=True, country=country)
    region.save()

    region = Region(id=13, name='Кировскаяобласть(Киров)', active=True, country=country)
    region.save()

    region = Region(id=14, name='Костромскаяобласть(Кострома)', active=True, country=country)
    region.save()

    region = Region(id=15, name='Курганскаяобласть(Курган)', active=True, country=country)
    region.save()

    region = Region(id=16, name='Курскаяобласть(Курск)', active=True, country=country)
    region.save()

    region = Region(id=17, name='Ленинградскаяобласть(Санкт Петербург)', active=True, country=country)
    region.save()

    region = Region(id=19, name='Липецкаяобласть(Липецк)', active=True, country=country)
    region.save()

    region = Region(id=20, name='Магаданскаяобласть(Магадан)', active=True, country=country)
    region.save()

    region = Region(id=21, name='Московскаяобласть(Москва)', active=True, country=country)
    region.save()

    region = Region(id=22, name='Мурманскаяобласть(Мурманск)', active=True, country=country)
    region.save()

    region = Region(id=23, name='Нижегородскаяобласть(НижнийНовгород)', active=True, country=country)
    region.save()

    region = Region(id=24, name='Новгородскаяобласть(ВеликийНовгород)', active=True, country=country)
    region.save()

    region = Region(id=25, name='Новосибирскаяобласть(Новосибирск)', active=True, country=country)
    region.save()

    region = Region(id=26, name='Омскаяобласть(Омск)', active=True, country=country)
    region.save()

    region = Region(id=27, name='Оренбургскаяобласть(Оренбург)', active=True, country=country)
    region.save()

    region = Region(id=28, name='Орловскаяобласть(Орёл)', active=True, country=country)
    region.save()

    region = Region(id=29, name='Пензенскаяобласть(Пенза)', active=True, country=country)
    region.save()

    region = Region(id=30, name='Псковскаяобласть(Псков)', active=True, country=country)
    region.save()

    region = Region(id=31, name='Ростовскаяобласть(Ростов на Дону)', active=True, country=country)
    region.save()

    region = Region(id=32, name='Рязанскаяобласть(Рязань)', active=True, country=country)
    region.save()

    region = Region(id=33, name='Сахалинскаяобласть(Южно Сахалинск)', active=True, country=country)
    region.save()

    region = Region(id=34, name='Самарскаяобласть(Самара)', active=True, country=country)
    region.save()

    region = Region(id=35, name='Саратовскаяобласть(Саратов)', active=True, country=country)
    region.save()

    region = Region(id=36, name='Смоленскаяобласть(Смоленск)', active=True, country=country)
    region.save()

    region = Region(id=37, name='Свердловскаяобласть(Екатеринбург)', active=True, country=country)
    region.save()

    region = Region(id=38, name='Тамбовскаяобласть(Тамбов)', active=True, country=country)
    region.save()

    region = Region(id=39, name='Томскаяобласть(Томск)', active=True, country=country)
    region.save()

    region = Region(id=40, name='Тверскаяобласть(Тверь)', active=True, country=country)
    region.save()

    region = Region(id=41, name='Тульскаяобласть(Тула)', active=True, country=country)
    region.save()

    region = Region(id=42, name='Тюменскаяобласть(Тюмень)', active=True, country=country)
    region.save()

    region = Region(id=43, name='Ульяновскаяобласть(Ульяновск)', active=True, country=country)
    region.save()

    region = Region(id=44, name='Владимирскаяобласть(Владимир)', active=True, country=country)
    region.save()

    region = Region(id=45, name='Волгоградскаяобласть(Волгоград)', active=True, country=country)
    region.save()

    region = Region(id=46, name='Вологодскаяобласть(Вологда)', active=True, country=country)
    region.save()

    region = Region(id=47, name='Воронежскаяобласть(Воронеж)', active=True, country=country)
    region.save()

    region = Region(id=48, name='Ярославскаяобласть(Ярославль)', active=True, country=country)
    region.save()


    country = Country(id=2, name='Кыргызстан', active=True)
    country.save()
    region = Region(name='г. Бишкек', active=True, country=country)
    region.save()
    region = Region(name='г. Ош', active=True, country=country)
    region.save()
    region = Region(name='Баткенская область', active=True, country=country)
    region.save()
    region = Region(name='Джалал-Абадская область', active=True, country=country)
    region.save()
    region = Region(name='Иссык-Кульская область', active=True, country=country)
    region.save()
    region = Region(name='Нарынская область', active=True, country=country)
    region.save()
    region = Region(name='Ошская область', active=True, country=country)
    region.save()
    region = Region(name='Таласская область', active=True, country=country)
    region.save()
    region = Region(name='Чуйская область', active=True, country=country)
    region.save()

    country = Country(id=3, name='Казахстан', active=True)
    country.save()
    region = Region(name='Нур-Султан (Астана)', active=True, country=country)
    region.save()
    region = Region(name='Алматы', active=True, country=country)
    region.save()
    region = Region(name='Шымкент', active=True, country=country)
    region.save()
    region = Region(name='Байконыр', active=True, country=country)
    region.save()
    region = Region(name='Акмолинская область', active=True, country=country)
    region.save()
    region = Region(name='Актюбинская область', active=True, country=country)
    region.save()
    region = Region(name='Алматинская область', active=True, country=country)
    region.save()
    region = Region(name='Атырауская область', active=True, country=country)
    region.save()
    region = Region(name='Восточно-Казахстанская область', active=True, country=country)
    region.save()
    region = Region(name='Жамбылская область', active=True, country=country)
    region.save()
    region = Region(name='Западно-Казахстанская область', active=True, country=country)
    region.save()
    region = Region(name='Карагандинская область', active=True, country=country)
    region.save()
    region = Region(name='Костанайская область', active=True, country=country)
    region.save()
    region = Region(name='Кызылординская область', active=True, country=country)
    region.save()
    region = Region(name='Мангистауская область', active=True, country=country)
    region.save()
    region = Region(name='Павлодарская область', active=True, country=country)
    region.save()
    region = Region(name='Севрено-Казахстанская область', active=True, country=country)
    region.save()
    region = Region(name='Туркестанская область', active=True, country=country)
    region.save()

    country = Country(id=4, name='Таджикистан', active=True)
    country.save()
    region = Region(name='г. Душанбе', active=True, country=country)
    region.save()
    region = Region(name='Горно - Бажахшанская область', active=True, country=country)
    region.save()
    region = Region(name='Согдийская область', active=True, country=country)
    region.save()
    region = Region(name='Хатлонская область', active=True, country=country)
    region.save()
    region = Region(name='Районы республиканского подчинения', active=True, country=country)
    region.save()

    country = Country(id=5, name='Туркменистан', active=True)
    country.save()
    region = Region(name='г. Ашхабад', active=True, country=country)
    region.save()
    region = Region(name='Ахалский велаят', active=True, country=country)
    region.save()
    region = Region(name='Балканский велаят', active=True, country=country)
    region.save()
    region = Region(name='Дашогузский велаят', active=True, country=country)
    region.save()
    region = Region(name='Лебапский велаят', active=True, country=country)
    region.save()
    region = Region(name='Марыйский велаят', active=True, country=country)
    region.save()


    print("EmployeesCount")
    EmployeesCount = apps.get_model("strike", "EmployeesCount")
    emps_count = EmployeesCount(id=1, choice='до 50 человек', active=True)
    emps_count.save()
    emps_count = EmployeesCount(id=2, choice='от 50 до 200 человек', active=True)
    emps_count.save()
    emps_count = EmployeesCount(id=3, choice='от 200 до 1500 человек', active=True)
    emps_count.save()
    emps_count = EmployeesCount(id=4, choice='более 1500 человек', active=True)
    emps_count.save()

    print('ParticipantsCount')
    ParticipantsCount = apps.get_model("strike", "ParticipantsCount")
    count = ParticipantsCount(id=1, choice='менее 10 человек', active=True)
    count.save()
    count = ParticipantsCount(id=2, choice='10-50 человек', active=True)
    count.save()
    count = ParticipantsCount(id=3, choice='51-100 человек', active=True)
    count.save()
    count = ParticipantsCount(id=4, choice='101-1000 человек', active=True)
    count.save()
    count = ParticipantsCount(id=5, choice='более 1000 человек', active=True)
    count.save()

    DemandType = apps.get_model("strike", "DemandType")
    type1 = DemandType(id=1, demand='Экономический', active=True)
    type1.save()
    type2 = DemandType(id=2, demand='Политический', active=True)
    type2.save()
    type3 = DemandType(id=3, demand='Смешанный', active=True)
    type3.save()

    DemandCategory = apps.get_model("strike", "DemandCategory")
    cat = DemandCategory(id=1,name='Оплата труда',demand_type=type1,active=True)
    cat.save()
    cat = DemandCategory(id=2,name='Охрана труда и здоровье',demand_type=type1,active=True)
    cat.save()
    cat = DemandCategory(id=3,name='Вопросы занятости уволенных/сокращенных работников, безработных',demand_type=type1,active=True)
    cat.save()
    cat = DemandCategory(id=4,name='Сокращение рабочего времени',demand_type=type1,active=True)
    cat.save()
    cat = DemandCategory(id=5,name='Другое',demand_type=type1,active=True)
    cat.save()

    cat = DemandCategory(id=6, name='Смена руководства предприятия', demand_type=type2, active=True)
    cat.save()
    cat = DemandCategory(id=7, name='Смена руководителей исполнительной власти', demand_type=type2, active=True)
    cat.save()
    cat = DemandCategory(id=8, name='Проведение политических реформ в стране', demand_type=type2, active=True)
    cat.save()
    cat = DemandCategory(id=9, name='Другое', demand_type=type2, active=True)
    cat.save()

    cat = DemandCategory(id=10, name='Требования связанные с профсоюзной деятельностью', demand_type=type3, active=True)
    cat.save()
    cat = DemandCategory(id=11, name='Другое', demand_type=type3, active=True)
    cat.save()

    OwnerShipType = apps.get_model("strike", "OwnerShipType")
    type = OwnerShipType(id=1, name='Национальная, государственная', active=True)
    type.save()
    type = OwnerShipType(id=2, name='Национальная, частная', active=True)
    type.save()
    type = OwnerShipType(id=3, name='Смешанная', active=True)
    type.save()
    type = OwnerShipType(id=4, name='Иностранная', active=True)
    type.save()

    Age = apps.get_model("strike", "Age")
    age = Age(id=1, name='менее 18 лет', active=True)
    age.save()
    age = Age(id=2, name='19-62', active=True)
    age.save()
    age = Age(id=3, name='63 и старше', active=True)
    age.save()


    GroupCharacter = apps.get_model("strike", "GroupCharacter")
    group_character = GroupCharacter(id=1,name='Бригада или производственная группа', active=True)
    group_character.save()
    group_character = GroupCharacter(id=2,name='Определенная категория работников', active=True)
    group_character.save()
    group_character = GroupCharacter(id=3,name='Другое', active=True)
    group_character.save()

    TradeUnionGroupMembership = apps.get_model("strike", "TradeUnionGroupMembership")
    tradeUnionGroupMembership = TradeUnionGroupMembership(id=1, name='Все состоят в профсоюзе', active=True)
    tradeUnionGroupMembership.save()
    tradeUnionGroupMembership = TradeUnionGroupMembership(id=2, name='В профсоюзе состоят не все', active=True)
    tradeUnionGroupMembership.save()
    tradeUnionGroupMembership = TradeUnionGroupMembership(id=3, name='Никто не состоит в профсоюзе', active=True)
    tradeUnionGroupMembership.save()

    Initiator = apps.get_model("strike", "Initiator")
    initiator = Initiator(id=1,name="Профсоюз")
    initiator.save()
    initiator = Initiator(id=2,name="Группа лиц")
    initiator.save()
    initiator = Initiator(id=3,name="Физическое лицо")
    initiator.save()
    initiator = Initiator(id=4,name="Работодатель")
    initiator.save()

    TradeunionChoice = apps.get_model("strike", "TradeunionChoice")
    tradeunion_choice = TradeunionChoice(id=1, name='Да', active=True)
    tradeunion_choice.save()
    tradeunion_choice = TradeunionChoice(id=2, name='Отсутствует', active=True)
    tradeunion_choice.save()
    tradeunion_choice = TradeunionChoice(id=3, name='Неизвестно', active=True)
    tradeunion_choice.save()
    tradeunion_choice = TradeunionChoice(id=4, name='Другое', active=True)
    tradeunion_choice.save()
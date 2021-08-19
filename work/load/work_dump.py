def load_works(apps, schema_editor):

    # print('TradeunionMembership')
    # TradeunionMembership = apps.get_model("work", "TradeunionMembership")
    # tradeunionMembership = TradeunionMembership(id=1, name="все члены профсоюза", active=True)
    # tradeunionMembership.save()
    # tradeunionMembership = TradeunionMembership(id=2, name="большинство члены профсоюза", active=True)
    # tradeunionMembership.save()
    # tradeunionMembership = TradeunionMembership(id=3, name="меньшая часть члены профсоюза", active=True)
    # tradeunionMembership.save()
    # tradeunionMembership = TradeunionMembership(id=4, name="нет членов профсоюза", active=True)
    # tradeunionMembership.save()
    # tradeunionMembership = TradeunionMembership(id=5, name="другое", active=True)
    # tradeunionMembership.save()

    print('TradeUnionCount')
    TradeUnionCount = apps.get_model("work", "TradeUnionCount")
    tradeUnionCount = TradeUnionCount(id=1, choice="Численность сократилась", active=True)
    tradeUnionCount.save()
    tradeUnionCount = TradeUnionCount(id=2, choice="Численность увеличилась", active=True)
    tradeUnionCount.save()
    tradeUnionCount = TradeUnionCount(id=3, choice="Численность сохранилась", active=True)
    tradeUnionCount.save()

    print('TradeUnionSituation')
    TradeUnionSituation = apps.get_model("work", "TradeUnionSituation")
    tradeUnionSituation = TradeUnionSituation(id=1, name="Продолжает действовать", active=True)
    tradeUnionSituation.save()
    tradeUnionSituation = TradeUnionSituation(id=2, name="Продолжает существовать, но не действует", active=True)
    tradeUnionSituation.save()
    tradeUnionSituation = TradeUnionSituation(id=3, name="Прекратил существование", active=True)
    tradeUnionSituation.save()
    tradeUnionSituation = TradeUnionSituation(id=4, name="Другое", active=True)
    tradeUnionSituation.save()

    print('VictimSituation')
    VictimSituation = apps.get_model("work", "VictimSituation")
    victimSituation = VictimSituation(id=1, name="Продолжает (ют) работать", active=True)
    victimSituation.save()
    victimSituation = VictimSituation(id=2, name="Уволен(ы) под давлением работодателя", active=True)
    victimSituation.save()
    victimSituation = VictimSituation(id=3, name="Прекратил(и) работать добровольно", active=True)
    victimSituation.save()
    victimSituation = VictimSituation(id=4, name="Другое", active=True)
    victimSituation.save()

    print('NatureViolation')
    NatureViolation = apps.get_model("work", "NatureViolation")
    natureViolation = NatureViolation(id=1, name="Разовое", active=True)
    natureViolation.save()
    natureViolation = NatureViolation(id=2, name="Системное", active=True)
    natureViolation.save()

    print('RightsState')
    RightsState = apps.get_model("work", "RightsState")
    rightsState = RightsState(id=1, name="Права восстановлены", active=True)
    rightsState.save()
    rightsState = RightsState(id=2, name="Права не восстановлены", active=True)
    rightsState.save()
    rightsState = RightsState(id=3, name="Права восстановлены частично", active=True)
    rightsState.save()
    rightsState = RightsState(id=4, name="Другое ", active=True)
    rightsState.save()


    print('MembershipOfGroupPersons')
    MembershipOfGroupPersons = apps.get_model("work", "MembershipOfGroupPersons")
    membershipOfGroupPersons = MembershipOfGroupPersons(id=1, name="все члены профсоюза", active=True)
    membershipOfGroupPersons.save()
    membershipOfGroupPersons = MembershipOfGroupPersons(id=2, name="большинство члены профсоюза", active=True)
    membershipOfGroupPersons.save()
    membershipOfGroupPersons = MembershipOfGroupPersons(id=3, name="меньшая часть члены профсоюза", active=True)
    membershipOfGroupPersons.save()
    membershipOfGroupPersons = MembershipOfGroupPersons(id=4, name="нет членов профсоюза", active=True)
    membershipOfGroupPersons.save()
    membershipOfGroupPersons = MembershipOfGroupPersons(id=5, name="другое", active=True)
    membershipOfGroupPersons.save()

    print('GroupType')
    GroupType = apps.get_model("work", "GroupType")
    groupType = GroupType(id=1, name="бригада или производственная группа", active=True)
    groupType.save()
    groupType = GroupType(id=2, name="определенная категория работников", active=True)
    groupType.save()
    groupType = GroupType(id=3, name="работники, защищающие права свои или других", active=True)
    groupType.save()
    groupType = GroupType(id=4, name="другое", active=True)
    groupType.save()

    print("AgreementDetail")
    AgreementDetail = apps.get_model("work", "AgreementDetail")
    agreementDetail = AgreementDetail(id=1, name="Договор есть, но он не трудовой, а гражданско-правовой", active=True)
    agreementDetail.save()
    agreementDetail = AgreementDetail(id=2, name="Договор подписывал, но он остался у работодателя", active=True)
    agreementDetail.save()
    agreementDetail = AgreementDetail(id=3, name="Договор подписывал, но он остался у посредника", active=True)
    agreementDetail.save()
    # agreementDetail = AgreementDetail(id=4, name="Подписан трудовой договор", active=True)
    # agreementDetail.save()

    print("Education")
    Education = apps.get_model("work", "Education")
    education = Education(id=1, name="Незаконченное среднее", active=True)
    education.save()
    education = Education(id=2, name="Среднее общее/среднее техническое (средняя школа, ПТУ)", active=True)
    education.save()
    education = Education(id=3, name="Среднее специальное (техникум, колледж)", active=True)
    education.save()
    education = Education(id=4, name="Незаконченное высшее (Вуз не менее 3 курсов)", active=True)
    education.save()
    education = Education(id=5, name="Высшее (бакалавриат, специалитет)", active=True)
    education.save()
    education = Education(id=6, name="Магистратура", active=True)
    education.save()
    education = Education(id=7, name="Ученая степень /несколько высших образований", active=True)
    education.save()

    print("MaritalStatus")
    MaritalStatus = apps.get_model("work", "MaritalStatus")
    maritalStatus = MaritalStatus(id=1, name="Женат /замужем", active=True)
    maritalStatus.save()
    maritalStatus = MaritalStatus(id=2, name="Разведен (а)", active=True)
    maritalStatus.save()
    maritalStatus = MaritalStatus(id=3, name="В неофициальном браке", active=True)
    maritalStatus.save()
    maritalStatus = MaritalStatus(id=4, name="Живет раздельно (разошедшийся)", active=True)
    maritalStatus.save()
    maritalStatus = MaritalStatus(id=5, name="Вдовец/вдова", active=True)
    maritalStatus.save()
    maritalStatus = MaritalStatus(id=6, name="Никогда не состоял(а) в браке", active=True)
    maritalStatus.save()

    Intruder = apps.get_model("work", "Intruder")
    intruder = Intruder(id=1,name="Государственные органы",active=True)
    intruder.save()
    intruder = Intruder(id=2,name="Органы местного самоуправления ",active=True)
    intruder.save()
    intruder = Intruder(id=3,name="Правоохранительные органы",active=True)
    intruder.save()
    intruder = Intruder(id=4,name="Работодатель (компания)",active=True)
    intruder.save()
    intruder = Intruder(id=5,name="Затрудняюсь ответить",active=True)
    intruder.save()
    intruder = Intruder(id=6,name="Другое ",active=True)
    intruder.save()



    Victim = apps.get_model("work", "Victim")
    victim = Victim(id=1,name="профсоюзная организация",active=True)
    victim.save()
    victim = Victim(id=2,name="физическое лицо",active=True)
    victim.save()
    victim = Victim(id=3,name="группа лиц (работников)",active=True)
    victim.save()

    Source = apps.get_model("work", "Source")
    source = Source(id=1, name='информация о нарушении, допущенном в отношении человека лично', active=True)
    source.save()
    source = Source(id=2, name='интервью с пострадавшим', active=True)
    source.save()
    source = Source(id=3, name='сообщение в СМИ', active=True)
    source.save()
    source = Source(id=4, name='информация от профсоюзов', active=True)
    source.save()
    source = Source(id=5, name='информация НКО, правозащитной организации', active=True)
    source.save()
    source = Source(id=6, name='информация от работодателя', active=True)
    source.save()
    source = Source(id=7, name='информация от правоохранительных органов', active=True)
    source.save()
    source = Source(id=8, name='информация от государственного органа', active=True)
    source.save()
    source = Source(id=9, name='информация от представителя интересов пострадавшего (юриста)', active=True)
    source.save()
    source = Source(id=10, name='другое', active=True)
    source.save()

    print("Gender")
    Gender = apps.get_model("work", "Gender")
    gender = Gender(name='мужской', active=True)
    gender.save()
    gender = Gender(name='женский ', active=True)
    gender.save()


    print("EmployeesCount")
    EmployeesCount = apps.get_model("work", "EmployeesCount")
    employeesCount = EmployeesCount(name='от 10 до 50 человек', active=True)
    employeesCount.save()
    employeesCount = EmployeesCount(name='малое до 50 человек', active=True)
    employeesCount.save()
    employeesCount = EmployeesCount(name='среднее от 50 до 200 чел', active=True)
    employeesCount.save()
    employeesCount = EmployeesCount(name='крупное от 200 до 1000 чел.', active=True)
    employeesCount.save()
    employeesCount = EmployeesCount(name='очень большое - свыше 1000 чел.', active=True)
    employeesCount.save()

    print("OwnerShipType")
    OwnerShipType = apps.get_model("work", "OwnerShipType")
    ownerShipType = OwnerShipType(name='Национальная, государственная', active=True)
    ownerShipType.save()
    ownerShipType = OwnerShipType(name='Национальная, частная', active=True)
    ownerShipType.save()
    ownerShipType = OwnerShipType(name='Иностранная', active=True)
    ownerShipType.save()
    ownerShipType = OwnerShipType(name='Смешанная', active=True)
    ownerShipType.save()

    print("Country")
    Country = apps.get_model("work", "Country")
    country = Country(id=1, name='Россия', active=True)
    country.save()
    Region = apps.get_model("work", "Region")

    region = Region(name='г.Москва', active=True, country=country)
    region.save()

    region = Region(name='Амурскаяобласть(Благовещенск)', active=True, country=country)
    region.save()

    region = Region(name='Архангельскаяобласть(Архангельск)', active=True, country=country)
    region.save()

    region = Region(name='Астраханскаяобласть(Астрахань)', active=True, country=country)
    region.save()

    region = Region(name='Белгородскаяобласть(Белгород)', active=True, country=country)
    region.save()

    region = Region(name='Брянскаяобласть(Брянск)', active=True, country=country)
    region.save()

    region = Region(name='Челябинскаяобласть(Челябинск)', active=True, country=country)
    region.save()

    region = Region(name='Иркутскаяобласть(Иркутск)', active=True, country=country)
    region.save()

    region = Region(name='Ивановскаяобласть(Иваново)', active=True, country=country)
    region.save()

    region = Region(name='Калининградскаяобласть(Калининград)', active=True, country=country)
    region.save()

    region = Region(name='Калужскаяобласть(Калуга)', active=True, country=country)
    region.save()

    region = Region(name='Кемеровскаяобласть—Кузбасс(Кемерово)', active=True, country=country)
    region.save()

    region = Region(name='Кировскаяобласть(Киров)', active=True, country=country)
    region.save()

    region = Region(name='Костромскаяобласть(Кострома)', active=True, country=country)
    region.save()

    region = Region(name='Курганскаяобласть(Курган)', active=True, country=country)
    region.save()

    region = Region(name='Курскаяобласть(Курск)', active=True, country=country)
    region.save()

    region = Region(name='Ленинградскаяобласть(Санкт Петербург)', active=True, country=country)
    region.save()

    region = Region(name='Липецкаяобласть(Липецк)', active=True, country=country)
    region.save()

    region = Region(name='Магаданскаяобласть(Магадан)', active=True, country=country)
    region.save()

    region = Region(name='Московскаяобласть(Москва)', active=True, country=country)
    region.save()

    region = Region(name='Мурманскаяобласть(Мурманск)', active=True, country=country)
    region.save()

    region = Region(name='Нижегородскаяобласть(НижнийНовгород)', active=True, country=country)
    region.save()

    region = Region(name='Новгородскаяобласть(ВеликийНовгород)', active=True, country=country)
    region.save()

    region = Region(name='Новосибирскаяобласть(Новосибирск)', active=True, country=country)
    region.save()

    region = Region(name='Омскаяобласть(Омск)', active=True, country=country)
    region.save()

    region = Region(name='Оренбургскаяобласть(Оренбург)', active=True, country=country)
    region.save()

    region = Region(name='Орловскаяобласть(Орёл)', active=True, country=country)
    region.save()

    region = Region(name='Пензенскаяобласть(Пенза)', active=True, country=country)
    region.save()

    region = Region(name='Псковскаяобласть(Псков)', active=True, country=country)
    region.save()

    region = Region(name='Ростовскаяобласть(Ростов на Дону)', active=True, country=country)
    region.save()

    region = Region(name='Рязанскаяобласть(Рязань)', active=True, country=country)
    region.save()

    region = Region(name='Сахалинскаяобласть(Южно Сахалинск)', active=True, country=country)
    region.save()

    region = Region(name='Самарскаяобласть(Самара)', active=True, country=country)
    region.save()

    region = Region(name='Саратовскаяобласть(Саратов)', active=True, country=country)
    region.save()

    region = Region(name='Смоленскаяобласть(Смоленск)', active=True, country=country)
    region.save()

    region = Region(name='Свердловскаяобласть(Екатеринбург)', active=True, country=country)
    region.save()

    region = Region(name='Тамбовскаяобласть(Тамбов)', active=True, country=country)
    region.save()

    region = Region(name='Томскаяобласть(Томск)', active=True, country=country)
    region.save()

    region = Region(name='Тверскаяобласть(Тверь)', active=True, country=country)
    region.save()

    region = Region(name='Тульскаяобласть(Тула)', active=True, country=country)
    region.save()

    region = Region(name='Тюменскаяобласть(Тюмень)', active=True, country=country)
    region.save()

    region = Region(name='Ульяновскаяобласть(Ульяновск)', active=True, country=country)
    region.save()

    region = Region(name='Владимирскаяобласть(Владимир)', active=True, country=country)
    region.save()

    region = Region(name='Волгоградскаяобласть(Волгоград)', active=True, country=country)
    region.save()

    region = Region(name='Вологодскаяобласть(Вологда)', active=True, country=country)
    region.save()

    region = Region(name='Воронежскаяобласть(Воронеж)', active=True, country=country)
    region.save()

    region = Region(name='Ярославскаяобласть(Ярославль)', active=True, country=country)
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

    country = Country(id=6, name='Узбекистан', active=True)
    country.save()
    region = Region(name='Андижанская область', active=True, country=country)
    region.save()
    region = Region(name='Бухарская область', active=True, country=country)
    region.save()
    region = Region(name='Джизакская область', active=True, country=country)
    region.save()
    region = Region(name='Кашкадарьинская область', active=True, country=country)
    region.save()
    region = Region(name='Навоийская область', active=True, country=country)
    region.save()
    region = Region(name='Наманганская область ', active=True, country=country)
    region.save()
    region = Region(name='Республика Каракалпакстан', active=True, country=country)
    region.save()
    region = Region(name='Самаркандская область', active=True, country=country)
    region.save()
    region = Region(name='Сурхандарьинская область', active=True, country=country)
    region.save()
    region = Region(name='Сырдарьинская область', active=True, country=country)
    region.save()
    region = Region(name='Ташкент область', active=True, country=country)
    region.save()
    region = Region(name='Ферганская область', active=True, country=country)
    region.save()
    region = Region(name='Хорезмская область', active=True, country=country)
    region.save()

    GroupOfRights = apps.get_model("work", "GroupOfRights")
    groupOfRights = GroupOfRights(id=1, name='Нарушение в сфере профсоюзных прав и гражданских свобод', active=True)
    groupOfRights.save()
    groupOfRights = GroupOfRights(id=2,
                                  name='Нарушения положений Конвенций МОТ № 87 «Относительно свободы ассоциаций и защиты права на организацию»',
                                  active=True)
    groupOfRights.save()
    groupOfRights = GroupOfRights(id=3,
                                  name='Нарушения положений Конвенций МОТ № 98 «Относительно применения принципов права на организацию и заключение коллективных договоров»',
                                  active=True)
    groupOfRights.save()
    groupOfRights = GroupOfRights(id=4,
                                  name='Нарушения положений Конвенций МОТ №135 «О защите прав представителей, трудящихся на предприятии и предоставляемых им возможностям»',
                                  active=True)
    groupOfRights.save()

    groupOfRights = GroupOfRights(id=5, name='Проведение консультаций', active=True)
    groupOfRights.save()

    groupOfRights = GroupOfRights(id=6, name='Принцип запрещения дискриминации', active=True)
    groupOfRights.save()
    groupOfRights = GroupOfRights(id=7, name='Использование детского труда', active=True)
    groupOfRights.save()

    groupOfRights = GroupOfRights(id=8, name='Запрет принудительного труда', active=True)
    groupOfRights.save()

    TradeUnionRight = apps.get_model("work", "TradeUnionRight")
    tradeUnionRight = TradeUnionRight(id=1, name="Обвинения в преступном поведении в связи с профсоюзной деятельностью")
    tradeUnionRight.save()
    tradeUnionRight = TradeUnionRight(id=2, name="Нарушения права на жизнь, безопасность, физическую и моральную неприкосновенность личности")
    tradeUnionRight.save()
    tradeUnionRight = TradeUnionRight(id=3, name="Нарушения права на проведение собраний и демонстраций")
    tradeUnionRight.save()
    tradeUnionRight = TradeUnionRight(id=4, name="Нарушения в области свободы мнений и слова")
    tradeUnionRight.save()
    tradeUnionRight = TradeUnionRight(id=5, name="Требования раскрытия информации о членстве в профсоюзе и профсоюзной деятельности")
    tradeUnionRight.save()
    tradeUnionRight = TradeUnionRight(id=6, name="Защита профсоюзных помещений и имущества профсоюзов")
    tradeUnionRight.save()
    tradeUnionRight = TradeUnionRight(id=7, name="Другое")
    tradeUnionRight.save()

    Сonvention87 = apps.get_model("work", "Сonvention87")
    convention87 = Сonvention87(
        name="Нарушение права трудящихся без какого-либо различия создавать организации без предварительного разрешения",
        )
    convention87.save()
    convention87 = Сonvention87(
        name="Нарушение права свободно создавать профсоюзы и вступать в профсоюзы только лишь на условии подчинения уставу",
        )
    convention87.save()
    convention87 = Сonvention87(name="Нарушение права профсоюза самостоятельно вырабатывать свои уставы и положения",
                                )
    convention87.save()
    convention87 = Сonvention87(name="Нарушение права свободно выбирать своих представителей",
                                )
    convention87.save()
    convention87 = Сonvention87(name="Нарушения права профсоюза организовывать деятельность своего аппарата",
                                )
    convention87.save()
    convention87 = Сonvention87(
        name="Нарушение права профсоюза свободно организовывать свою деятельность и формулировать свою программу действий",
        )
    convention87.save()
    convention87 = Сonvention87(name="Нарушение права на забастовку",
                                )
    convention87.save()
    convention87 = Сonvention87(
        name="Нарушение права на создание федераций и конфедераций и на вступление в международные организации",
        )
    convention87.save()
    convention87 = Сonvention87(name="Принудительный роспуск и приостановление деятельности профсоюза",
                                )
    convention87.save()


    Сonvention98 = apps.get_model("work", "Сonvention98")
    convention98 = Сonvention98( name="Антипрофсоюзная дискриминация",
                                      )
    convention98.save()
    convention98 = Сonvention98( name="Нарушения права на проведение коллективных переговоров",
                                      )
    convention98.save()

    # rightsViolation = RightsViolation(id=19, name="Непредставление времени для участия в профсоюзных собраниях",
    #                                   )
    # rightsViolation.save()
    # rightsViolation = RightsViolation(id=20, name="Воспрепятствование в сборе профсоюзных взносов",
    #                                   )
    # rightsViolation.save()
    # rightsViolation = RightsViolation(id=21, name="Ограничение доступа представителей профсоюза на рабочие места",
    #                                   )
    # rightsViolation.save()
    # rightsViolation = RightsViolation(id=22, name="Другое",
    #                                   )
    # rightsViolation.save()
    #
    # rightsViolation = RightsViolation(id=23, name="Непроведение консультаций относительно докладов Правительства в МОТ",
    #                                   )
    # rightsViolation.save()
    # rightsViolation = RightsViolation(id=24, name="Непроведение консультаций в период подготовки и редактирования законодательства",
    #                                   )
    # rightsViolation.save()
    # rightsViolation = RightsViolation(id=25, name="Непроведение консультаций в процессе реструктурирования, рационализации и сокращения персонала",
    #                                   )
    # rightsViolation.save()
    # rightsViolation = RightsViolation(id=26, name="Другое",
    #                                   )
    # rightsViolation.save()


    PrincipleOfNonDiscrimination = apps.get_model("work", "PrincipleOfNonDiscrimination")
    principleOfNonDiscrimination = PrincipleOfNonDiscrimination( name="Дискриминация по различным основаниям",
                                      )
    principleOfNonDiscrimination.save()
    principleOfNonDiscrimination = PrincipleOfNonDiscrimination( name="Дискриминация в различных сферах трудовых отношений",
                                      )
    principleOfNonDiscrimination.save()
    principleOfNonDiscrimination = PrincipleOfNonDiscrimination(name="Нарушения в области проведения государственной политики по искоренению дискриминации и поощрению равенства прав и возможностей",
                                      )
    principleOfNonDiscrimination.save()



    TradeUnionCrime = apps.get_model("work", "TradeUnionCrime")
    tradeUnionCrime = TradeUnionCrime(id=1, name="арест, задержание")
    tradeUnionCrime.save()
    tradeUnionCrime = TradeUnionCrime(id=2, name="осуждение по уголовному делу")
    tradeUnionCrime.save()
    tradeUnionCrime = TradeUnionCrime(id=3, name="другое")
    tradeUnionCrime.save()

    MeetingsRight = apps.get_model("work", "MeetingsRight")
    meetingsRight = MeetingsRight(id=1, name="ограничения права на собрание организаций в их помещениях")
    meetingsRight.save()
    meetingsRight = MeetingsRight(id=2, name="ограничения на проведения публичных собраний и демонстраций")
    meetingsRight.save()
    meetingsRight = MeetingsRight(id=3, name="ограничения на участие в международных профсоюзных встречах",
                                      )
    meetingsRight.save()
    meetingsRight = MeetingsRight(id=4, name="другое",)
    meetingsRight.save()

    TradeUnionBuildingsRight = apps.get_model("work", "TradeUnionBuildingsRight")
    tradeUnionBuildingsRight = TradeUnionBuildingsRight(id=1, name="принудительная конфискация имущества профсоюза",
                                      )
    tradeUnionBuildingsRight.save()
    tradeUnionBuildingsRight = TradeUnionBuildingsRight(id=2, name="неправомерно вторжение в помещение профсоюза",
                                      )
    tradeUnionBuildingsRight.save()
    tradeUnionBuildingsRight = TradeUnionBuildingsRight(id=3, name="другое",
                                      )
    tradeUnionBuildingsRight.save()



    CreateOrganizationRight = apps.get_model("work", "CreateOrganizationRight")
    createOrganizationRight = CreateOrganizationRight(id=1, name="Нарушения права создавать профсоюз без какого бы то ни было различия",
                                              )
    createOrganizationRight.save()
    createOrganizationRight = CreateOrganizationRight(id=2, name="Нарушение права создавать профсоюз без предварительного разрешения",
                                              )
    createOrganizationRight.save()
    createOrganizationRight = CreateOrganizationRight(id=3, name="Требования получения одобрения работодателя в каких-либо формах",
                                              )
    createOrganizationRight.save()
    createOrganizationRight = CreateOrganizationRight(id=4, name="Юридические формальности, препятствующие созданию профсоюза",
                                              )
    createOrganizationRight.save()
    createOrganizationRight = CreateOrganizationRight(id=5, name="Завышенные требования к минимальной численности",
                                              )
    createOrganizationRight.save()
    createOrganizationRight = CreateOrganizationRight(id=6, name="Необоснованный отказ в регистрации профсоюза",
                                              )
    createOrganizationRight.save()
    createOrganizationRight = CreateOrganizationRight(id=7, name="Другое",
                                              )
    createOrganizationRight.save()

    CreateTradeUnionRight = apps.get_model("work", "CreateTradeUnionRight")
    createTradeUnionRight = CreateTradeUnionRight(id=1, name="Установления работодателем принципов профсоюзной структуры и единства профсоюза",
                                              )
    createTradeUnionRight.save()
    createTradeUnionRight = CreateTradeUnionRight(id=2, name="Санкции за попытки создания профсоюза",
                                              )
    createTradeUnionRight.save()
    createTradeUnionRight = CreateTradeUnionRight(id=3, name="Фаворитизм или дискриминация в отношении определённых профсоюзов",
                                              )
    createTradeUnionRight.save()
    createTradeUnionRight = CreateTradeUnionRight(id=4, name="Право вступать в профсоюзы по своему выбору",
                                              )
    createTradeUnionRight.save()
    createTradeUnionRight = CreateTradeUnionRight(id=5, name="Другие",
                                              )
    createTradeUnionRight.save()


    ElectionsRight = apps.get_model("work", "ElectionsRight")
    electionsRight = ElectionsRight(id=1, name="Установление требований к выборным представителям",
                                              )
    electionsRight.save()
    electionsRight = ElectionsRight(id=2, name="Вмешательство в проведение профсоюзных выборов",
                                              )
    electionsRight.save()
    electionsRight = ElectionsRight(id=3, name="Другие",
                                              )
    electionsRight.save()


    TradeUnionActivityRight = apps.get_model("work", "TradeUnionActivityRight")

    tradeUnionActivityRight = TradeUnionActivityRight(id=1, name="Контроль над внутренней жизнью профсоюза",
                                              )
    tradeUnionActivityRight.save()
    tradeUnionActivityRight = TradeUnionActivityRight(id=2, name="Вмешательство в ведение финансовой деятельности",
                                              )
    tradeUnionActivityRight.save()
    tradeUnionActivityRight = TradeUnionActivityRight(id=3, name="Проверки профсоюзных документов без обоснования причин",
                                              )
    tradeUnionActivityRight.save()
    tradeUnionActivityRight = TradeUnionActivityRight(id=4, name="Другое",
                                              )
    tradeUnionActivityRight.save()


    CreateStrikeRight = apps.get_model("work", "CreateStrikeRight")

    createStrikeRight = CreateStrikeRight(id=1, name="Цели забастовки",
                                              )
    createStrikeRight.save()
    createStrikeRight = CreateStrikeRight(id=2, name="Виды забастовок",
                                              )
    createStrikeRight.save()
    createStrikeRight = CreateStrikeRight(id=3, name="Предварительные условия и процедуры для проведения забастовок",
                                              )
    createStrikeRight.save()
    createStrikeRight = CreateStrikeRight(id=4, name="Объявление забастовки незаконной",
                                              )
    createStrikeRight.save()
    createStrikeRight = CreateStrikeRight(id=5, name="Ограничение и запрещение забастовок",
                                              )
    createStrikeRight.save()
    createStrikeRight = CreateStrikeRight(id=6, name="Минимум необходимых работ",
                                              )
    createStrikeRight.save()
    createStrikeRight = CreateStrikeRight(id=7, name="Вмешательство властей и работодателя в проведение забастовки",
                                              )
    createStrikeRight.save()
    createStrikeRight = CreateStrikeRight(id=8, name="Санкции за участие в забастовке",
                                              )
    createStrikeRight.save()
    createStrikeRight = CreateStrikeRight(id=9, name="Дискриминация лиц, участвующих в забастовке",
                                              )
    createStrikeRight.save()
    createStrikeRight = CreateStrikeRight(id=10, name="Другое",
                                              )
    createStrikeRight.save()

    AntiTradeUnionDiscrimination = apps.get_model("work", "AntiTradeUnionDiscrimination")
    antiTradeUnionDiscrimination = AntiTradeUnionDiscrimination(id=1, name="Увольнения профсоюзных активистов",)
    antiTradeUnionDiscrimination.save()
    antiTradeUnionDiscrimination = AntiTradeUnionDiscrimination(id=2, name="Незаконные переводы, отправление в простой и иные формы дискриминации",
                                              )
    antiTradeUnionDiscrimination.save()
    antiTradeUnionDiscrimination = AntiTradeUnionDiscrimination(id=3, name="Давление на членов профсоюза",
                                              )
    antiTradeUnionDiscrimination.save()
    antiTradeUnionDiscrimination = AntiTradeUnionDiscrimination(id=4, name="Эффективная защита от дискриминации",
                                              )
    antiTradeUnionDiscrimination.save()
    antiTradeUnionDiscrimination = AntiTradeUnionDiscrimination(id=5, name="Другое",)
    antiTradeUnionDiscrimination.save()


    СonversationRight = apps.get_model("work", "СonversationRight")

    conversationRight = СonversationRight(id=1, name="Нарушение принципа добросовестности ведения переговоров",
                                              )
    conversationRight.save()
    conversationRight = СonversationRight(id=2, name="Непризнание за профсоюзом права на коллективные переговоры (в т.ч. вопросы представительности профсоюзов)",
                                              )
    conversationRight.save()
    conversationRight = СonversationRight(id=3, name="Нарушение свободных и добровольных переговоров",
                                              )
    conversationRight.save()
    conversationRight = СonversationRight(id=4, name="Вмешательство властей в проведение коллективных переговоров",
                                              )
    conversationRight.save()
    conversationRight = СonversationRight(id=5, name="Отказ в обсуждении определённых вопросов",
                                              )
    conversationRight.save()
    conversationRight = СonversationRight(id=6, name="Отказ работодателя предоставить необходимую информацию для проведения коллективных переговоров",
                                              )
    conversationRight.save()
    conversationRight = СonversationRight(id=7, name="Отказ органов государственной власти регистрировать коллективный договор",
                                              )
    conversationRight.save()
    conversationRight = СonversationRight(id=8, name="Другие",
                                              )
    conversationRight.save()

    Сonvention135 = apps.get_model("work", "Сonvention135")
    convention135 = Сonvention135(id=1, name="Непредставление времени для участия в профсоюзных собраниях",
                                  )
    convention135.save()
    convention135 = Сonvention135(id=2, name="Воспрепятствование в сборе профсоюзных взносов",
                                  )
    convention135.save()
    convention135 = Сonvention135(id=3, name="Ограничение доступа представителей профсоюза на рабочие места",
                                  )
    convention135.save()
    convention135 = Сonvention135(id=4, name="Другое",
                                  )
    convention135.save()

    ConsultationRight = apps.get_model("work", "ConsultationRight")
    consultationRight = ConsultationRight(id=1, name="Непроведение консультаций относительно докладов Правительства в МОТ",
                                      )
    consultationRight.save()
    consultationRight = ConsultationRight(id=2, name="Непроведение консультаций в период подготовки и редактирования законодательства",
                                      )
    consultationRight.save()
    consultationRight = ConsultationRight(id=3, name="Непроведение консультаций в процессе реструктурирования, рационализации и сокращения персонала",
                                      )
    consultationRight.save()
    consultationRight = ConsultationRight(id=4, name="Другое",
                                      )
    consultationRight.save()

    DiscriminatiOnVariousGrounds = apps.get_model("work", "DiscriminatiOnVariousGrounds")
    discriminatiOnVariousGrounds = DiscriminatiOnVariousGrounds(id=1, name="Дискриминация по основаниям, перечисленным в Конвенции №111",
                                              )
    discriminatiOnVariousGrounds.save()
    discriminatiOnVariousGrounds = DiscriminatiOnVariousGrounds(id=2, name="Дискриминация по основаниям, устанавливаемым национальным законодательством",
                                              )
    discriminatiOnVariousGrounds.save()

    DiscriminationInVariousAreas = apps.get_model("work", "DiscriminationInVariousAreas")
    discriminationInVariousAreas = DiscriminationInVariousAreas(id=1, name="Доступ к профориентации и трудоустройству",
                                              )
    discriminationInVariousAreas.save()
    discriminationInVariousAreas = DiscriminationInVariousAreas(id=2, name="Доступ к обучению и занятости по своему выбору",
                                              )
    discriminationInVariousAreas.save()
    discriminationInVariousAreas = DiscriminationInVariousAreas(id=3, name="Возможности карьерного роста и продвижения по службе на основе индивидуальных качеств",
                                              )
    discriminationInVariousAreas.save()
    discriminationInVariousAreas = DiscriminationInVariousAreas(id=4, name="Доступ к гарантиям сохранения занятости",
                                              )
    discriminationInVariousAreas.save()
    discriminationInVariousAreas = DiscriminationInVariousAreas(id=5, name="Оплата труда",
                                              )
    discriminationInVariousAreas.save()
    discriminationInVariousAreas = DiscriminationInVariousAreas(id=6, name="Рабочее время и время отдыха",
                                              )
    discriminationInVariousAreas.save()
    discriminationInVariousAreas = DiscriminationInVariousAreas(id=7, name="Безопасность условий труда на работе",
                                              )
    discriminationInVariousAreas.save()
    discriminationInVariousAreas = DiscriminationInVariousAreas(id=8, name="Доступ к социальному обеспечению и медицинскому обслуживанию",
                                              )
    discriminationInVariousAreas.save()
    discriminationInVariousAreas = DiscriminationInVariousAreas(id=9, name="Доступ к членству в объединениях работников или работодателей и к участию в их делах",
                                              )
    discriminationInVariousAreas.save()
    discriminationInVariousAreas = DiscriminationInVariousAreas(id=10, name="Другое",
                                              )
    discriminationInVariousAreas.save()


    PublicPolicyDiscrimination = apps.get_model("work", "PublicPolicyDiscrimination")
    publicPolicyDiscrimination = PublicPolicyDiscrimination(id=1, name="Отказ от разработки и проведения государственной политики",
                                              )
    publicPolicyDiscrimination.save()
    publicPolicyDiscrimination = PublicPolicyDiscrimination(id=2, name="Нарушения в сфере антидискриминационного законодательства и практики его применения",
                                              )
    publicPolicyDiscrimination.save()
    publicPolicyDiscrimination = PublicPolicyDiscrimination(id=3, name="Нарушения в сфере социального диалога",
                                              )
    publicPolicyDiscrimination.save()
    publicPolicyDiscrimination = PublicPolicyDiscrimination(id=4, name="Непринятие органами власти мер для предотвращения дискриминации",
                                              )
    publicPolicyDiscrimination.save()


    ChildLabor = apps.get_model("work", "ChildLabor")
    childLabor = ChildLabor(id=1, name="Нарушение положений Конвенции МОТ № 138 «О минимальном возрасте для приема на работу»",
                                      )
    childLabor.save()
    childLabor = ChildLabor(id=2,
                                      name="Нарушения Конвенции МОТ № 182 «О запрещении и немедленных мерах по искоренению наихудших форм детского труда»",
                                      )
    childLabor.save()

    Сonvention138 = apps.get_model("work", "Сonvention138")
    convention138 = Сonvention138(id=1, name="Использование труда детей моложе минимального возраста (не опасные работы)",
                                              )
    convention138.save()
    convention138 = Сonvention138(id=2, name="Использование детского труда на опасной работе (ОР)",
                                              )
    convention138.save()
    convention138 = Сonvention138(id=3, name="Нарушения Рекомендации МОТ №146 «О минимальном возрасте для приема на работу»",
                                              )
    convention138.save()


    Сonvention182 = apps.get_model("work", "Сonvention182")
    convention182 = Сonvention182(id=1, name="Привлечение детей к «наихудшим формам детского труда»",
                                              )
    convention182.save()
    convention182 = Сonvention182(id=2, name="Нарушения на уровне государственной политики",
                                              )
    convention182.save()


    ProhibitionOfForcedLabor = apps.get_model("work", "ProhibitionOfForcedLabor")
    prohibitionOfForcedLabor = ProhibitionOfForcedLabor(id=1,
                                      name="Использование принудительного труда в случаях, прямо запрещенных Конвенциями МОТ №29 и №105",
                                      )
    prohibitionOfForcedLabor.save()
    prohibitionOfForcedLabor = ProhibitionOfForcedLabor(id=2,
                                      name="Косвенное принуждение государством к труду (Рекомендация МОТ № 35 О косвенном принуждении к труду)",
                                      )
    prohibitionOfForcedLabor.save()
    prohibitionOfForcedLabor = ProhibitionOfForcedLabor(id=3,
                                      name="Нарушения при использовании принудительного (обязательного) труда в допустимых случаях (Конвенция МОТ №29 Относительно принудительного или обязательного труда)",
                                      )
    prohibitionOfForcedLabor.save()
    prohibitionOfForcedLabor = ProhibitionOfForcedLabor(id=4,
                                      name="Нарушения, связанные с непринятием государством системных мер",
                                      )
    prohibitionOfForcedLabor.save()



    UseOfForcedLabor = apps.get_model("work", "UseOfForcedLabor")
    useOfForcedLabor = UseOfForcedLabor(id=1, name="В пользу частных лиц и компаний",
                                              )
    useOfForcedLabor.save()
    useOfForcedLabor = UseOfForcedLabor(id=2, name="Для выполнения подземных работ в шахтах",
                                              )
    useOfForcedLabor.save()
    useOfForcedLabor = UseOfForcedLabor(id=3, name="В качестве коллективного наказания, применяемые к коллективу в целом, за преступления, совершенные какими-либо из его членов",
                                              )
    useOfForcedLabor.save()
    useOfForcedLabor = UseOfForcedLabor(id=4, name="В качестве средства или меры наказания",
                                              )
    useOfForcedLabor.save()



    GovernmentCoercion = apps.get_model("work", "GovernmentCoercion")
    governmentCoercion = GovernmentCoercion(id=1, name="Принятие решений о развитии территорий без учета способности населения к труду, жизненных и трудовых привычек",
                                              )
    governmentCoercion.save()
    governmentCoercion = GovernmentCoercion(id=2, name="Экономическое давление с целью заставить искать работу по найму",
                                              )
    governmentCoercion.save()
    governmentCoercion = GovernmentCoercion(id=3, name="Введение ограничений добровольного перехода в иные виды занятости или районы (косвенное принуждение к работе в определенных отраслях или районах)",
                                              )
    governmentCoercion.save()


    ViolationsUsingCompulsoryLabor = apps.get_model("work", "ViolationsUsingCompulsoryLabor")

    violationsUsingCompulsoryLabor = ViolationsUsingCompulsoryLabor(id=1, name="Привлечение к принудительному (обязательному) труду в ситуации, когда отсутствуют условия, позволяющие использовать принудительный труд",
                                              )
    violationsUsingCompulsoryLabor.save()
    violationsUsingCompulsoryLabor = ViolationsUsingCompulsoryLabor(id=2, name="Привлечение к принудительному труду лиц запрещенных категорий",
                                              )
    violationsUsingCompulsoryLabor.save()
    violationsUsingCompulsoryLabor = ViolationsUsingCompulsoryLabor(id=3, name="Несоблюдение ограничений при привлечении к принудительному (обязательному труду)",
                                              )
    violationsUsingCompulsoryLabor.save()
    violationsUsingCompulsoryLabor = ViolationsUsingCompulsoryLabor(id=4, name="Нарушения при оплате принудительного (обязательного) труда",
                                              )
    violationsUsingCompulsoryLabor.save()
    violationsUsingCompulsoryLabor = ViolationsUsingCompulsoryLabor(id=5, name="Нарушения при несчастных случаях и профзаболеваниях лиц, привлекавшихся к принудительному труду",
                                              )
    violationsUsingCompulsoryLabor.save()
    violationsUsingCompulsoryLabor = ViolationsUsingCompulsoryLabor(id=6, name="Нарушения в сфере охраны труда (здоровье и безопасность)",
                                              )
    violationsUsingCompulsoryLabor.save()
    violationsUsingCompulsoryLabor = ViolationsUsingCompulsoryLabor(id=7, name="Нарушения при привлечении к строительным или ремонтным работам на длительное время",
                                              )
    violationsUsingCompulsoryLabor.save()
    violationsUsingCompulsoryLabor = ViolationsUsingCompulsoryLabor(id=8, name="Нарушения при привлечении к принудительному труду для перевозки лиц или грузов в отсутствие изданной регламентации",
                                              )
    violationsUsingCompulsoryLabor.save()
    violationsUsingCompulsoryLabor = ViolationsUsingCompulsoryLabor(id=9, name="Нарушения при привлечении к принудительной обработке земли",
                                              )
    violationsUsingCompulsoryLabor.save()

    FailureSystemicMeasures = apps.get_model("work", "FailureSystemicMeasures")

    failureSystemicMeasures = FailureSystemicMeasures(id=1,
                                                      name="Отсутствие полной регламентации применения принудительного или обязательного труда государством",
                                                      )
    failureSystemicMeasures.save()
    failureSystemicMeasures = FailureSystemicMeasures(id=2,
                                                      name="Отсутствие возможности у трудящихся предъявлять претензии по поводу их привлечения к принудительному труду и / или отсутствие гарантий рассмотрения и учета претензий",
                                                      )
    failureSystemicMeasures.save()
    failureSystemicMeasures = FailureSystemicMeasures(id=3,
                                                      name="Необеспечение строгого соблюдения правил использования принудительного труда, в частности отсутствие компетентного органа надзора",
                                                      )
    failureSystemicMeasures.save()
    failureSystemicMeasures = FailureSystemicMeasures(id=4,
                                                      name="Необеспечение уголовного преследования лиц, незаконно использующих принудительный труд",
                                                      )
    failureSystemicMeasures.save()
    failureSystemicMeasures = FailureSystemicMeasures(id=5,
                                                      name="Непринятие мер, предусмотренных в Рекомендации, МОТ № 203",
                                                      )
    failureSystemicMeasures.save()

    TradeUnionActivities = apps.get_model("work", "TradeUnionActivities")
    trade_union_activities = TradeUnionActivities(id=1, name="текстильная и легкая промышленность")
    trade_union_activities.save()
    trade_union_activities = TradeUnionActivities(id=2, name="здравоохранение")
    trade_union_activities.save()
    trade_union_activities = TradeUnionActivities(id=3, name="образование и наука ")
    trade_union_activities.save()
    trade_union_activities = TradeUnionActivities(id=4, name="строительство и производство ПСМ")
    trade_union_activities.save()
    trade_union_activities = TradeUnionActivities(id=5, name="горнодобывающая и металлургическая")
    trade_union_activities.save()
    trade_union_activities = TradeUnionActivities(id=6, name="государственная и муниципальная служба")
    trade_union_activities.save()
    trade_union_activities = TradeUnionActivities(id=7, name="коммунально-бытового обслуживания и предпринимательства")
    trade_union_activities.save()
    trade_union_activities = TradeUnionActivities(id=8, name="автомобильного и сельскохозяйственного машиностроения")
    trade_union_activities.save()
    trade_union_activities = TradeUnionActivities(id=9, name="энергетики и электротехнической промышленности")
    trade_union_activities.save()
    trade_union_activities = TradeUnionActivities(id=10, name="железнодорожников и транспортных строителей")
    trade_union_activities.save()
    trade_union_activities = TradeUnionActivities(id=11, name="лесного хозяйства")
    trade_union_activities.save()
    trade_union_activities = TradeUnionActivities(id=12, name="транспорт и дорожного хозяйства")
    trade_union_activities.save()
    trade_union_activities = TradeUnionActivities(id=13, name="агропромышленный комплекс")
    trade_union_activities.save()
    trade_union_activities = TradeUnionActivities(id=14, name="пищевой и перерабатывающей промышленности")
    trade_union_activities.save()
    trade_union_activities = TradeUnionActivities(id=15, name="связь")
    trade_union_activities.save()
    trade_union_activities = TradeUnionActivities(id=16, name="авиация")
    trade_union_activities.save()
    trade_union_activities = TradeUnionActivities(id=17, name="торговля, общественное питание, потребкооперация и другие формы предпринимательства")
    trade_union_activities.save()
    trade_union_activities = TradeUnionActivities(id=18, name="культура")
    trade_union_activities.save()
    trade_union_activities = TradeUnionActivities(id=19, name="Другое")
    trade_union_activities.save()

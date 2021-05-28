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

    Country = apps.get_model("work", "Country")
    Region = apps.get_model("work", "Region")

    country = Country(id=1, name='Россия', active=True)
    country.save()
    region = Region(id=1, name='г. Москва', active=True, country=country)
    region.save()

    country = Country(id=2, name='Кыргызстан', active=True)
    country.save()
    region = Region(id=2, name='г. Бишкек', active=True, country=country)
    region.save()
    region = Region(id=3, name='г. Ош', active=True, country=country)
    region.save()
    region = Region(id=4, name='Чуйская область', active=True, country=country)
    region.save()
    region = Region(id=5, name='Ошская область', active=True, country=country)
    region.save()
    region = Region(id=6, name='Баткенская область', active=True, country=country)
    region.save()
    region = Region(id=7, name='Джалал-Абадская область', active=True, country=country)
    region.save()
    region = Region(id=8, name='Иссык-Кульская область', active=True, country=country)
    region.save()
    region = Region(id=9, name='Нарынская область', active=True, country=country)
    region.save()
    region = Region(id=10, name='Таласская область', active=True, country=country)
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


    # rightsViolation = RightsViolation(id=8, name="Нарушение права трудящихся без какого-либо различия создавать организации без предварительного разрешения",
    #                                   )
    # rightsViolation.save()
    # rightsViolation = RightsViolation(id=9, name="Нарушение права свободно создавать профсоюзы и вступать в профсоюзы только лишь на условии подчинения уставу",
    #                                   )
    # rightsViolation.save()
    # rightsViolation = RightsViolation(id=10, name="Нарушение права профсоюза самостоятельно вырабатывать свои уставы и положения",
    #                                   )
    # rightsViolation.save()
    # rightsViolation = RightsViolation(id=11, name="Нарушение права свободно выбирать своих представителей",
    #                                   )
    # rightsViolation.save()
    # rightsViolation = RightsViolation(id=12, name="Нарушения права профсоюза организовывать деятельность своего аппарата",
    #                                   )
    # rightsViolation.save()
    # rightsViolation = RightsViolation(id=13, name="Нарушение права профсоюза свободно организовывать свою деятельность и формулировать свою программу действий",
    #                                   )
    # rightsViolation.save()
    # rightsViolation = RightsViolation(id=14, name="Нарушение права на забастовку",
    #                                   )
    # rightsViolation.save()
    # rightsViolation = RightsViolation(id=15, name="Нарушение права на создание федераций и конфедераций и на вступление в международные организации",
    #                                   )
    # rightsViolation.save()
    # rightsViolation = RightsViolation(id=16, name="Принудительный роспуск и приостановление деятельности профсоюза",
    #                                   )
    # rightsViolation.save()
    # rightsViolation = RightsViolation(id=17, name="Антипрофсоюзная дискриминация",
    #                                   )
    # rightsViolation.save()
    # rightsViolation = RightsViolation(id=18, name="Нарушения права на проведение коллективных переговоров",
    #                                   )
    # rightsViolation.save()
    #
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
    # rightsViolation = RightsViolation(id=27, name="Дискриминация по различным основаниям",
    #                                   )
    # rightsViolation.save()
    # rightsViolation = RightsViolation(id=28, name="Дискриминация в различных сферах трудовых отношений",
    #                                   )
    # rightsViolation.save()
    # rightsViolation = RightsViolation(id=29, name="Нарушения в области проведения государственной политики по искоренению дискриминации и поощрению равенства прав и возможностей",
    #                                   )
    # rightsViolation.save()
    # rightsViolation = RightsViolation(id=30, name="Нарушение положений Конвенции МОТ № 138 «О минимальном возрасте для приема на работу»",
    #                                   )
    # rightsViolation.save()
    # rightsViolation = RightsViolation(id=31,
    #                                   name="Нарушения Конвенции МОТ № 182 «О запрещении и немедленных мерах по искоренению наихудших форм детского труда»",
    #                                   )
    # rightsViolation.save()
    # rightsViolation = RightsViolation(id=32,
    #                                   name="Использование принудительного труда в случаях, прямо запрещенных Конвенциями МОТ №29 и №105",
    #                                   )
    # rightsViolation.save()
    # rightsViolation = RightsViolation(id=33,
    #                                   name="Косвенное принуждение государством к труду (Рекомендация МОТ № 35 О косвенном принуждении к труду)",
    #                                   )
    # rightsViolation.save()
    # rightsViolation = RightsViolation(id=34,
    #                                   name="Нарушения при использовании принудительного (обязательного) труда в допустимых случаях (Конвенция МОТ №29 Относительно принудительного или обязательного труда)",
    #                                   )
    # rightsViolation.save()
    # rightsViolation = RightsViolation(id=35,
    #                                   name="Нарушения, связанные с непринятием государством системных мер",
    #                                   )
    # rightsViolation.save()

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

    #
    #
    #
    #
    #
    #
    #
    # rightsViolationCase = RightsViolationCase(id=40, name="Увольнения профсоюзных активистов",
    #                                           )
    # rightsViolationCase.save()
    # rightsViolationCase = RightsViolationCase(id=41, name="Незаконные переводы, отправление в простой и иные формы дискриминации",
    #                                           )
    # rightsViolationCase.save()
    # rightsViolationCase = RightsViolationCase(id=42, name="Давление на членов профсоюза",
    #                                           )
    # rightsViolationCase.save()
    # rightsViolationCase = RightsViolationCase(id=43, name="Эффективная защита от дискриминации",
    #                                           )
    # rightsViolationCase.save()
    # rightsViolationCase = RightsViolationCase(id=44, name="Другое",
    #                                           )
    # rightsViolationCase.save()
    #
    #
    # rightsViolationCase = RightsViolationCase(id=45, name="Нарушение принципа добросовестности ведения переговоров",
    #                                           )
    # rightsViolationCase.save()
    # rightsViolationCase = RightsViolationCase(id=46, name="Непризнание за профсоюзом права на коллективные переговоры (в т.ч. вопросы представительности профсоюзов)",
    #                                           )
    # rightsViolationCase.save()
    # rightsViolationCase = RightsViolationCase(id=47, name="Нарушение свободных и добровольных переговоров",
    #                                           )
    # rightsViolationCase.save()
    # rightsViolationCase = RightsViolationCase(id=48, name="Вмешательство властей в проведение коллективных переговоров",
    #                                           )
    # rightsViolationCase.save()
    # rightsViolationCase = RightsViolationCase(id=49, name="Отказ в обсуждении определённых вопросов",
    #                                           )
    # rightsViolationCase.save()
    # rightsViolationCase = RightsViolationCase(id=50, name="Отказ работодателя предоставить необходимую информацию для проведения коллективных переговоров",
    #                                           )
    # rightsViolationCase.save()
    # rightsViolationCase = RightsViolationCase(id=51, name="Отказ органов государственной власти регистрировать коллективный договор",
    #                                           )
    # rightsViolationCase.save()
    # rightsViolationCase = RightsViolationCase(id=52, name="Другие",
    #                                           )
    # rightsViolationCase.save()
    #
    #
    # rightsViolationCase = RightsViolationCase(id=53, name="Дискриминация по основаниям, перечисленным в Конвенции №111",
    #                                           )
    # rightsViolationCase.save()
    # rightsViolationCase = RightsViolationCase(id=54, name="Дискриминация по основаниям, устанавливаемым национальным законодательством",
    #                                           )
    # rightsViolationCase.save()
    # rightsViolationCase = RightsViolationCase(id=55, name="Доступ к профориентации и трудоустройству",
    #                                           )
    # rightsViolationCase.save()
    # rightsViolationCase = RightsViolationCase(id=56, name="Доступ к обучению и занятости по своему выбору",
    #                                           )
    # rightsViolationCase.save()
    # rightsViolationCase = RightsViolationCase(id=57, name="Возможности карьерного роста и продвижения по службе на основе индивидуальных качеств",
    #                                           )
    # rightsViolationCase.save()
    # rightsViolationCase = RightsViolationCase(id=58, name="Доступ к гарантиям сохранения занятости",
    #                                           )
    # rightsViolationCase.save()
    # rightsViolationCase = RightsViolationCase(id=59, name="Оплата труда",
    #                                           )
    # rightsViolationCase.save()
    # rightsViolationCase = RightsViolationCase(id=60, name="Рабочее время и время отдыха",
    #                                           )
    # rightsViolationCase.save()
    # rightsViolationCase = RightsViolationCase(id=61, name="Безопасность условий труда на работе",
    #                                           )
    # rightsViolationCase.save()
    # rightsViolationCase = RightsViolationCase(id=62, name="Доступ к социальному обеспечению и медицинскому обслуживанию",
    #                                           )
    # rightsViolationCase.save()
    # rightsViolationCase = RightsViolationCase(id=63, name="Доступ к членству в объединениях работников или работодателей и к участию в их делах",
    #                                           )
    # rightsViolationCase.save()
    # rightsViolationCase = RightsViolationCase(id=64, name="Другое",
    #                                           )
    # rightsViolationCase.save()
    #
    #
    #
    # rightsViolationCase = RightsViolationCase(id=65, name="Отказ от разработки и проведения государственной политики",
    #                                           )
    # rightsViolationCase.save()
    # rightsViolationCase = RightsViolationCase(id=66, name="Нарушения в сфере антидискриминационного законодательства и практики его применения",
    #                                           )
    # rightsViolationCase.save()
    # rightsViolationCase = RightsViolationCase(id=67, name="Нарушения в сфере социального диалога",
    #                                           )
    # rightsViolationCase.save()
    # rightsViolationCase = RightsViolationCase(id=68, name="Непринятие органами власти мер для предотвращения дискриминации",
    #                                           )
    # rightsViolationCase.save()
    #
    #
    # rightsViolationCase = RightsViolationCase(id=69, name="Использование труда детей моложе минимального возраста (не опасные работы)",
    #                                           )
    # rightsViolationCase.save()
    # rightsViolationCase = RightsViolationCase(id=70, name="Использование детского труда на опасной работе (ОР)",
    #                                           )
    # rightsViolationCase.save()
    # rightsViolationCase = RightsViolationCase(id=71, name="Нарушения Рекомендации МОТ №146 «О минимальном возрасте для приема на работу»",
    #                                           )
    # rightsViolationCase.save()
    #
    #
    # rightsViolationCase = RightsViolationCase(id=72, name="Привлечение детей к «наихудшим формам детского труда»",
    #                                           )
    # rightsViolationCase.save()
    # rightsViolationCase = RightsViolationCase(id=73, name="Нарушения на уровне государственной политики",
    #                                           )
    # rightsViolationCase.save()
    #
    #
    #
    # rightsViolationCase = RightsViolationCase(id=74, name="В пользу частных лиц и компаний",
    #                                           )
    # rightsViolationCase.save()
    # rightsViolationCase = RightsViolationCase(id=75, name="Для выполнения подземных работ в шахтах",
    #                                           )
    # rightsViolationCase.save()
    # rightsViolationCase = RightsViolationCase(id=76, name="В качестве коллективного наказания, применяемые к коллективу в целом, за преступления, совершенные какими-либо из его членов",
    #                                           )
    # rightsViolationCase.save()
    # rightsViolationCase = RightsViolationCase(id=77, name="В качестве средства или меры наказания",
    #                                           )
    # rightsViolationCase.save()
    #
    #
    # rightsViolationCase = RightsViolationCase(id=78, name="Принятие решений о развитии территорий без учета способности населения к труду, жизненных и трудовых привычек",
    #                                           )
    # rightsViolationCase.save()
    # rightsViolationCase = RightsViolationCase(id=79, name="Экономическое давление с целью заставить искать работу по найму",
    #                                           )
    # rightsViolationCase.save()
    # rightsViolationCase = RightsViolationCase(id=80, name="Введение ограничений добровольного перехода в иные виды занятости или районы (косвенное принуждение к работе в определенных отраслях или районах)",
    #                                           )
    # rightsViolationCase.save()
    #
    #
    # rightsViolationCase = RightsViolationCase(id=81, name="Привлечение к принудительному (обязательному) труду в ситуации, когда отсутствуют условия, позволяющие использовать принудительный труд",
    #                                           )
    # rightsViolationCase.save()
    # rightsViolationCase = RightsViolationCase(id=82, name="Привлечение к принудительному труду лиц запрещенных категорий",
    #                                           )
    # rightsViolationCase.save()
    # rightsViolationCase = RightsViolationCase(id=83, name="Несоблюдение ограничений при привлечении к принудительному (обязательному труду)",
    #                                           )
    # rightsViolationCase.save()
    # rightsViolationCase = RightsViolationCase(id=84, name="Нарушения при оплате принудительного (обязательного) труда",
    #                                           )
    # rightsViolationCase.save()
    # rightsViolationCase = RightsViolationCase(id=85, name="Нарушения при несчастных случаях и профзаболеваниях лиц, привлекавшихся к принудительному труду",
    #                                           )
    # rightsViolationCase.save()
    # rightsViolationCase = RightsViolationCase(id=86, name="Нарушения в сфере охраны труда (здоровье и безопасность)",
    #                                           )
    # rightsViolationCase.save()
    # rightsViolationCase = RightsViolationCase(id=87, name="Нарушения при привлечении к строительным или ремонтным работам на длительное время",
    #                                           )
    # rightsViolationCase.save()
    # rightsViolationCase = RightsViolationCase(id=88, name="Нарушения при привлечении к принудительному труду для перевозки лиц или грузов в отсутствие изданной регламентации",
    #                                           )
    # rightsViolationCase.save()
    # rightsViolationCase = RightsViolationCase(id=89, name="Нарушения при привлечении к принудительной обработке земли",
    #                                           )
    # rightsViolationCase.save()
    #
    #
    # rightsViolationCase = RightsViolationCase(id=90, name="Отсутствие полной регламентации применения принудительного или обязательного труда государством",
    #                                           )
    # rightsViolationCase.save()
    # rightsViolationCase = RightsViolationCase(id=91, name="Отсутствие возможности у трудящихся предъявлять претензии по поводу их привлечения к принудительному труду и / или отсутствие гарантий рассмотрения и учета претензий",
    #                                           )
    # rightsViolationCase.save()
    # rightsViolationCase = RightsViolationCase(id=92, name="Необеспечение строгого соблюдения правил использования принудительного труда, в частности отсутствие компетентного органа надзора",
    #                                           )
    # rightsViolationCase.save()
    # rightsViolationCase = RightsViolationCase(id=93, name="Необеспечение уголовного преследования лиц, незаконно использующих принудительный труд",
    #                                           )
    # rightsViolationCase.save()
    # rightsViolationCase = RightsViolationCase(id=94, name="Непринятие мер, предусмотренных в Рекомендации, МОТ № 203",
    #                                           )
    # rightsViolationCase.save()

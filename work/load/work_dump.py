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
    source = Source(id=0, name='информация о нарушении, допущенном в отношении человека лично', active=True)
    source.save()
    source = Source(id=1, name='интервью с пострадавшим', active=True)
    source.save()
    source = Source(id=2, name='сообщение в СМИ', active=True)
    source.save()
    source = Source(id=3, name='информация от профсоюзов', active=True)
    source.save()
    source = Source(id=4, name='информация НКО, правозащитной организации', active=True)
    source.save()
    source = Source(id=5, name='информация от работодателя', active=True)
    source.save()
    source = Source(id=6, name='информация от правоохранительных органов', active=True)
    source.save()
    source = Source(id=7, name='информация от государственного органа', active=True)
    source.save()
    source = Source(id=8, name='информация от представителя интересов пострадавшего (юриста)', active=True)
    source.save()
    source = Source(id=9, name='другое', active=True)
    source.save()

    Country = apps.get_model("work", "Country")
    Region = apps.get_model("work", "Region")

    country = Country(id=0, name='Россия', active=True)
    country.save()
    region = Region(id=0, name='г. Москва', active=True, country=country)
    region.save()

    country = Country(id=1, name='Кыргызстан', active=True)
    country.save()
    region = Region(id=0, name='г. Бишкек', active=True, country=country)
    region.save()
    region = Region(id=1, name='г. Ош', active=True, country=country)
    region.save()
    region = Region(id=2, name='Чуйская область', active=True, country=country)
    region.save()
    region = Region(id=3, name='Ошская область', active=True, country=country)
    region.save()
    region = Region(id=4, name='Баткенская область', active=True, country=country)
    region.save()
    region = Region(id=5, name='Джалал-Абадская область', active=True, country=country)
    region.save()
    region = Region(id=6, name='Иссык-Кульская область', active=True, country=country)
    region.save()
    region = Region(id=7, name='Нарынская область', active=True, country=country)
    region.save()
    region = Region(id=8, name='Таласская область', active=True, country=country)
    region.save()

    GroupOfRights = apps.get_model("work", "GroupOfRights")
    groupOfRights = GroupOfRights(id=1, name='Нарушение в сфере профсоюзных прав и гражданских свобод', active=True)
    groupOfRights.save()

    RightsViolation = apps.get_model("work", "RightsViolation")
    rightsViolation = RightsViolation(id=1, name="Обвинения в преступном поведении в связи с профсоюзной деятельностью",
                                      groupOfRights=groupOfRights)
    rightsViolation.save()

    RightsViolationCase = apps.get_model("work", "RightsViolationCase")
    rightsViolationCase = RightsViolationCase(id=1, name="арест, задержание",
                                      rightsViolation=rightsViolation)
    rightsViolationCase.save()
    rightsViolationCase = RightsViolationCase(id=2, name="осуждение по уголовному делу",
                                      rightsViolation=rightsViolation)
    rightsViolationCase.save()
    rightsViolationCase = RightsViolationCase(id=3, name="другое",
                                      rightsViolation=rightsViolation)
    rightsViolationCase.save()

    rightsViolation = RightsViolation(id=2, name="Нарушения права на жизнь, безопасность, физическую и моральную неприкосновенность личности",
                                      groupOfRights=groupOfRights)
    rightsViolation.save()

    rightsViolation = RightsViolation(id=3, name="Нарушения права на проведение собраний и демонстраций",
                                      groupOfRights=groupOfRights)
    rightsViolation.save()

    rightsViolationCase = RightsViolationCase(id=4, name="ограничения права на собрание организаций в их помещениях",
                                      rightsViolation=rightsViolation)
    rightsViolationCase.save()
    rightsViolationCase = RightsViolationCase(id=5, name="ограничения на проведения публичных собраний и демонстраций",
                                      rightsViolation=rightsViolation)
    rightsViolationCase.save()
    rightsViolationCase = RightsViolationCase(id=6, name="ограничения на участие в международных профсоюзных встречах",
                                      rightsViolation=rightsViolation)
    rightsViolationCase.save()
    rightsViolationCase = RightsViolationCase(id=7, name="другое",
                                      rightsViolation=rightsViolation)
    rightsViolationCase.save()


    rightsViolation = RightsViolation(id=4, name="Нарушения в области свободы мнений и слова",
                                      groupOfRights=groupOfRights)
    rightsViolation.save()
    rightsViolation = RightsViolation(id=5, name="Требования раскрытия информации о членстве в профсоюзе и профсоюзной деятельности",
                                      groupOfRights=groupOfRights)
    rightsViolation.save()
    rightsViolation = RightsViolation(id=6, name="Защита профсоюзных помещений и имущества профсоюзов",
                                      groupOfRights=groupOfRights)
    rightsViolation.save()

    rightsViolationCase = RightsViolationCase(id=8, name="принудительная конфискация имущества профсоюза",
                                      rightsViolation=rightsViolation)
    rightsViolationCase.save()
    rightsViolationCase = RightsViolationCase(id=9, name="неправомерно вторжение в помещение профсоюза",
                                      rightsViolation=rightsViolation)
    rightsViolationCase.save()
    rightsViolationCase = RightsViolationCase(id=10, name="другое",
                                      rightsViolation=rightsViolation)
    rightsViolationCase.save()
    rightsViolation = RightsViolation(id=7, name="Другое",
                                      groupOfRights=groupOfRights)
    rightsViolation.save()

    #groupOfRights = 2
    groupOfRights = GroupOfRights(id=2,
                                  name='Нарушения положений Конвенций МОТ № 87 «Относительно свободы ассоциаций и защиты права на организацию»',
                                  active=True)
    groupOfRights.save()

    rightsViolation = RightsViolation(id=8, name="Нарушение права трудящихся без какого-либо различия создавать организации без предварительного разрешения",
                                      groupOfRights=groupOfRights)
    rightsViolation.save()
    rightsViolationCase = RightsViolationCase(id=11, name="Нарушения права создавать профсоюз без какого бы то ни было различия",
                                              rightsViolation=rightsViolation)
    rightsViolationCase.save()
    rightsViolationCase = RightsViolationCase(id=12, name="Нарушение права создавать профсоюз без предварительного разрешения",
                                              rightsViolation=rightsViolation)
    rightsViolationCase.save()
    rightsViolationCase = RightsViolationCase(id=13, name="Требования получения одобрения работодателя в каких-либо формах",
                                              rightsViolation=rightsViolation)
    rightsViolationCase.save()
    rightsViolationCase = RightsViolationCase(id=14, name="Юридические формальности, препятствующие созданию профсоюза",
                                              rightsViolation=rightsViolation)
    rightsViolationCase.save()
    rightsViolationCase = RightsViolationCase(id=15, name="Завышенные требования к минимальной численности",
                                              rightsViolation=rightsViolation)
    rightsViolationCase.save()
    rightsViolationCase = RightsViolationCase(id=16, name="Необоснованный отказ в регистрации профсоюза",
                                              rightsViolation=rightsViolation)
    rightsViolationCase.save()
    rightsViolationCase = RightsViolationCase(id=17, name="Другое",
                                              rightsViolation=rightsViolation)
    rightsViolationCase.save()

    rightsViolation = RightsViolation(id=9, name="Нарушение права свободно создавать профсоюзы и вступать в профсоюзы только лишь на условии подчинения уставу",
                                      groupOfRights=groupOfRights)
    rightsViolation.save()
    rightsViolationCase = RightsViolationCase(id=18, name="Установления работодателем принципов профсоюзной структуры и единства профсоюза",
                                              rightsViolation=rightsViolation)
    rightsViolationCase.save()
    rightsViolationCase = RightsViolationCase(id=19, name="Санкции за попытки создания профсоюза",
                                              rightsViolation=rightsViolation)
    rightsViolationCase.save()
    rightsViolationCase = RightsViolationCase(id=20, name="Фаворитизм или дискриминация в отношении определённых профсоюзов",
                                              rightsViolation=rightsViolation)
    rightsViolationCase.save()
    rightsViolationCase = RightsViolationCase(id=21, name="Право вступать в профсоюзы по своему выбору",
                                              rightsViolation=rightsViolation)
    rightsViolationCase.save()
    rightsViolationCase = RightsViolationCase(id=22, name="Другие",
                                              rightsViolation=rightsViolation)
    rightsViolationCase.save()

    rightsViolation = RightsViolation(id=10, name="Нарушение права профсоюза самостоятельно вырабатывать свои уставы и положения",
                                      groupOfRights=groupOfRights)
    rightsViolation.save()
    rightsViolation = RightsViolation(id=11, name="Нарушение права свободно выбирать своих представителей",
                                      groupOfRights=groupOfRights)
    rightsViolation.save()
    rightsViolationCase = RightsViolationCase(id=23, name="Установление требований к выборным представителям",
                                              rightsViolation=rightsViolation)
    rightsViolationCase.save()
    rightsViolationCase = RightsViolationCase(id=24, name="Вмешательство в проведение профсоюзных выборов",
                                              rightsViolation=rightsViolation)
    rightsViolationCase.save()
    rightsViolationCase = RightsViolationCase(id=25, name="Другие",
                                              rightsViolation=rightsViolation)
    rightsViolationCase.save()

    rightsViolation = RightsViolation(id=12, name="Нарушения права профсоюза организовывать деятельность своего аппарата",
                                      groupOfRights=groupOfRights)
    rightsViolation.save()
    rightsViolationCase = RightsViolationCase(id=26, name="Контроль над внутренней жизнью профсоюза",
                                              rightsViolation=rightsViolation)
    rightsViolationCase.save()
    rightsViolationCase = RightsViolationCase(id=27, name="Вмешательство в ведение финансовой деятельности",
                                              rightsViolation=rightsViolation)
    rightsViolationCase.save()
    rightsViolationCase = RightsViolationCase(id=28, name="Проверки профсоюзных документов без обоснования причин",
                                              rightsViolation=rightsViolation)
    rightsViolationCase.save()
    rightsViolationCase = RightsViolationCase(id=29, name="Другое",
                                              rightsViolation=rightsViolation)
    rightsViolationCase.save()

    rightsViolation = RightsViolation(id=13, name="Нарушение права профсоюза свободно организовывать свою деятельность и формулировать свою программу действий",
                                      groupOfRights=groupOfRights)
    rightsViolation.save()
    rightsViolation = RightsViolation(id=14, name="Нарушение права на забастовку",
                                      groupOfRights=groupOfRights)
    rightsViolation.save()
    rightsViolationCase = RightsViolationCase(id=30, name="Цели забастовки",
                                              rightsViolation=rightsViolation)
    rightsViolationCase.save()
    rightsViolationCase = RightsViolationCase(id=31, name="Виды забастовок",
                                              rightsViolation=rightsViolation)
    rightsViolationCase.save()
    rightsViolationCase = RightsViolationCase(id=32, name="Предварительные условия и процедуры для проведения забастовок",
                                              rightsViolation=rightsViolation)
    rightsViolationCase.save()
    rightsViolationCase = RightsViolationCase(id=33, name="Объявление забастовки незаконной",
                                              rightsViolation=rightsViolation)
    rightsViolationCase.save()
    rightsViolationCase = RightsViolationCase(id=34, name="Ограничение и запрещение забастовок",
                                              rightsViolation=rightsViolation)
    rightsViolationCase.save()
    rightsViolationCase = RightsViolationCase(id=35, name="Минимум необходимых работ",
                                              rightsViolation=rightsViolation)
    rightsViolationCase.save()
    rightsViolationCase = RightsViolationCase(id=36, name="Вмешательство властей и работодателя в проведение забастовки",
                                              rightsViolation=rightsViolation)
    rightsViolationCase.save()
    rightsViolationCase = RightsViolationCase(id=37, name="Санкции за участие в забастовке",
                                              rightsViolation=rightsViolation)
    rightsViolationCase.save()
    rightsViolationCase = RightsViolationCase(id=38, name="Дискриминация лиц, участвующих в забастовке",
                                              rightsViolation=rightsViolation)
    rightsViolationCase.save()
    rightsViolationCase = RightsViolationCase(id=39, name="Другое",
                                              rightsViolation=rightsViolation)
    rightsViolationCase.save()

    rightsViolation = RightsViolation(id=15, name="Нарушение права на создание федераций и конфедераций и на вступление в международные организации",
                                      groupOfRights=groupOfRights)
    rightsViolation.save()
    rightsViolation = RightsViolation(id=16, name="Принудительный роспуск и приостановление деятельности профсоюза",
                                      groupOfRights=groupOfRights)
    rightsViolation.save()




    groupOfRights = GroupOfRights(id=3,
                                  name='Нарушения положений Конвенций МОТ № 98 «Относительно применения принципов права на организацию и заключение коллективных договоров»',
                                  active=True)
    groupOfRights.save()
    rightsViolation = RightsViolation(id=17, name="Антипрофсоюзная дискриминация",
                                      groupOfRights=groupOfRights)
    rightsViolation.save()
    rightsViolationCase = RightsViolationCase(id=40, name="Увольнения профсоюзных активистов",
                                              rightsViolation=rightsViolation)
    rightsViolationCase.save()
    rightsViolationCase = RightsViolationCase(id=41, name="Незаконные переводы, отправление в простой и иные формы дискриминации",
                                              rightsViolation=rightsViolation)
    rightsViolationCase.save()
    rightsViolationCase = RightsViolationCase(id=42, name="Давление на членов профсоюза",
                                              rightsViolation=rightsViolation)
    rightsViolationCase.save()
    rightsViolationCase = RightsViolationCase(id=43, name="Эффективная защита от дискриминации",
                                              rightsViolation=rightsViolation)
    rightsViolationCase.save()
    rightsViolationCase = RightsViolationCase(id=44, name="Другое",
                                              rightsViolation=rightsViolation)
    rightsViolationCase.save()

    rightsViolation = RightsViolation(id=18, name="Нарушения права на проведение коллективных переговоров",
                                      groupOfRights=groupOfRights)
    rightsViolation.save()
    rightsViolationCase = RightsViolationCase(id=45, name="Нарушение принципа добросовестности ведения переговоров",
                                              rightsViolation=rightsViolation)
    rightsViolationCase.save()
    rightsViolationCase = RightsViolationCase(id=46, name="Непризнание за профсоюзом права на коллективные переговоры (в т.ч. вопросы представительности профсоюзов)",
                                              rightsViolation=rightsViolation)
    rightsViolationCase.save()
    rightsViolationCase = RightsViolationCase(id=47, name="Нарушение свободных и добровольных переговоров",
                                              rightsViolation=rightsViolation)
    rightsViolationCase.save()
    rightsViolationCase = RightsViolationCase(id=48, name="Вмешательство властей в проведение коллективных переговоров",
                                              rightsViolation=rightsViolation)
    rightsViolationCase.save()
    rightsViolationCase = RightsViolationCase(id=49, name="Отказ в обсуждении определённых вопросов",
                                              rightsViolation=rightsViolation)
    rightsViolationCase.save()
    rightsViolationCase = RightsViolationCase(id=50, name="Отказ работодателя предоставить необходимую информацию для проведения коллективных переговоров",
                                              rightsViolation=rightsViolation)
    rightsViolationCase.save()
    rightsViolationCase = RightsViolationCase(id=51, name="Отказ органов государственной власти регистрировать коллективный договор",
                                              rightsViolation=rightsViolation)
    rightsViolationCase.save()
    rightsViolationCase = RightsViolationCase(id=52, name="Другие",
                                              rightsViolation=rightsViolation)
    rightsViolationCase.save()

    groupOfRights = GroupOfRights(id=4,
                                  name='Нарушения положений Конвенций МОТ №135 «О защите прав представителей, трудящихся на предприятии и предоставляемых им возможностям»',
                                  active=True)
    groupOfRights.save()
    rightsViolation = RightsViolation(id=19, name="Непредставление времени для участия в профсоюзных собраниях",
                                      groupOfRights=groupOfRights)
    rightsViolation.save()
    rightsViolation = RightsViolation(id=20, name="Воспрепятствование в сборе профсоюзных взносов",
                                      groupOfRights=groupOfRights)
    rightsViolation.save()
    rightsViolation = RightsViolation(id=21, name="Ограничение доступа представителей профсоюза на рабочие места",
                                      groupOfRights=groupOfRights)
    rightsViolation.save()
    rightsViolation = RightsViolation(id=22, name="Другое",
                                      groupOfRights=groupOfRights)
    rightsViolation.save()

    groupOfRights = GroupOfRights(id=5, name='Проведение консультаций', active=True)
    groupOfRights.save()
    rightsViolation = RightsViolation(id=23, name="Непроведение консультаций относительно докладов Правительства в МОТ",
                                      groupOfRights=groupOfRights)
    rightsViolation.save()
    rightsViolation = RightsViolation(id=24, name="Непроведение консультаций в период подготовки и редактирования законодательства",
                                      groupOfRights=groupOfRights)
    rightsViolation.save()
    rightsViolation = RightsViolation(id=25, name="Непроведение консультаций в процессе реструктурирования, рационализации и сокращения персонала",
                                      groupOfRights=groupOfRights)
    rightsViolation.save()
    rightsViolation = RightsViolation(id=26, name="Другое",
                                      groupOfRights=groupOfRights)
    rightsViolation.save()

    groupOfRights = GroupOfRights(id=6, name='Принцип запрещения дискриминации', active=True)
    groupOfRights.save()
    rightsViolation = RightsViolation(id=27, name="Дискриминация по различным основаниям",
                                      groupOfRights=groupOfRights)
    rightsViolation.save()
    rightsViolationCase = RightsViolationCase(id=53, name="Дискриминация по основаниям, перечисленным в Конвенции №111",
                                              rightsViolation=rightsViolation)
    rightsViolationCase.save()
    rightsViolationCase = RightsViolationCase(id=54, name="Дискриминация по основаниям, устанавливаемым национальным законодательством",
                                              rightsViolation=rightsViolation)
    rightsViolationCase.save()
    rightsViolation = RightsViolation(id=28, name="Дискриминация в различных сферах трудовых отношений",
                                      groupOfRights=groupOfRights)
    rightsViolation.save()
    rightsViolationCase = RightsViolationCase(id=55, name="Доступ к профориентации и трудоустройству",
                                              rightsViolation=rightsViolation)
    rightsViolationCase.save()
    rightsViolationCase = RightsViolationCase(id=56, name="Доступ к обучению и занятости по своему выбору",
                                              rightsViolation=rightsViolation)
    rightsViolationCase.save()
    rightsViolationCase = RightsViolationCase(id=57, name="Возможности карьерного роста и продвижения по службе на основе индивидуальных качеств",
                                              rightsViolation=rightsViolation)
    rightsViolationCase.save()
    rightsViolationCase = RightsViolationCase(id=58, name="Доступ к гарантиям сохранения занятости",
                                              rightsViolation=rightsViolation)
    rightsViolationCase.save()
    rightsViolationCase = RightsViolationCase(id=59, name="Оплата труда",
                                              rightsViolation=rightsViolation)
    rightsViolationCase.save()
    rightsViolationCase = RightsViolationCase(id=60, name="Рабочее время и время отдыха",
                                              rightsViolation=rightsViolation)
    rightsViolationCase.save()
    rightsViolationCase = RightsViolationCase(id=61, name="Безопасность условий труда на работе",
                                              rightsViolation=rightsViolation)
    rightsViolationCase.save()
    rightsViolationCase = RightsViolationCase(id=62, name="Доступ к социальному обеспечению и медицинскому обслуживанию",
                                              rightsViolation=rightsViolation)
    rightsViolationCase.save()
    rightsViolationCase = RightsViolationCase(id=63, name="Доступ к членству в объединениях работников или работодателей и к участию в их делах",
                                              rightsViolation=rightsViolation)
    rightsViolationCase.save()
    rightsViolationCase = RightsViolationCase(id=64, name="Другое",
                                              rightsViolation=rightsViolation)
    rightsViolationCase.save()


    rightsViolation = RightsViolation(id=29, name="Нарушения в области проведения государственной политики по искоренению дискриминации и поощрению равенства прав и возможностей",
                                      groupOfRights=groupOfRights)
    rightsViolation.save()
    rightsViolationCase = RightsViolationCase(id=65, name="Отказ от разработки и проведения государственной политики",
                                              rightsViolation=rightsViolation)
    rightsViolationCase.save()
    rightsViolationCase = RightsViolationCase(id=66, name="Нарушения в сфере антидискриминационного законодательства и практики его применения",
                                              rightsViolation=rightsViolation)
    rightsViolationCase.save()
    rightsViolationCase = RightsViolationCase(id=67, name="Нарушения в сфере социального диалога",
                                              rightsViolation=rightsViolation)
    rightsViolationCase.save()
    rightsViolationCase = RightsViolationCase(id=68, name="Непринятие органами власти мер для предотвращения дискриминации",
                                              rightsViolation=rightsViolation)
    rightsViolationCase.save()

    groupOfRights = GroupOfRights(id=7, name='Использование детского труда', active=True)
    groupOfRights.save()
    rightsViolation = RightsViolation(id=30, name="Нарушение положений Конвенции МОТ № 138 «О минимальном возрасте для приема на работу»",
                                      groupOfRights=groupOfRights)
    rightsViolation.save()
    rightsViolationCase = RightsViolationCase(id=69, name="Использование труда детей моложе минимального возраста (не опасные работы)",
                                              rightsViolation=rightsViolation)
    rightsViolationCase.save()
    rightsViolationCase = RightsViolationCase(id=70, name="Использование детского труда на опасной работе (ОР)",
                                              rightsViolation=rightsViolation)
    rightsViolationCase.save()
    rightsViolationCase = RightsViolationCase(id=71, name="Нарушения Рекомендации МОТ №146 «О минимальном возрасте для приема на работу»",
                                              rightsViolation=rightsViolation)
    rightsViolationCase.save()

    rightsViolation = RightsViolation(id=31,
                                      name="Нарушения Конвенции МОТ № 182 «О запрещении и немедленных мерах по искоренению наихудших форм детского труда»",
                                      groupOfRights=groupOfRights)
    rightsViolation.save()
    rightsViolationCase = RightsViolationCase(id=72, name="Привлечение детей к «наихудшим формам детского труда»",
                                              rightsViolation=rightsViolation)
    rightsViolationCase.save()
    rightsViolationCase = RightsViolationCase(id=73, name="Нарушения на уровне государственной политики",
                                              rightsViolation=rightsViolation)
    rightsViolationCase.save()

    groupOfRights = GroupOfRights(id=8, name='Запрет принудительного труда', active=True)
    groupOfRights.save()
    rightsViolation = RightsViolation(id=32,
                                      name="Использование принудительного труда в случаях, прямо запрещенных Конвенциями МОТ №29 и №105",
                                      groupOfRights=groupOfRights)
    rightsViolation.save()
    rightsViolationCase = RightsViolationCase(id=74, name="В пользу частных лиц и компаний",
                                              rightsViolation=rightsViolation)
    rightsViolationCase.save()
    rightsViolationCase = RightsViolationCase(id=75, name="Для выполнения подземных работ в шахтах",
                                              rightsViolation=rightsViolation)
    rightsViolationCase.save()
    rightsViolationCase = RightsViolationCase(id=76, name="В качестве коллективного наказания, применяемые к коллективу в целом, за преступления, совершенные какими-либо из его членов",
                                              rightsViolation=rightsViolation)
    rightsViolationCase.save()
    rightsViolationCase = RightsViolationCase(id=77, name="В качестве средства или меры наказания",
                                              rightsViolation=rightsViolation)
    rightsViolationCase.save()

    rightsViolation = RightsViolation(id=33,
                                      name="Косвенное принуждение государством к труду (Рекомендация МОТ № 35 О косвенном принуждении к труду)",
                                      groupOfRights=groupOfRights)
    rightsViolation.save()
    rightsViolationCase = RightsViolationCase(id=78, name="Принятие решений о развитии территорий без учета способности населения к труду, жизненных и трудовых привычек",
                                              rightsViolation=rightsViolation)
    rightsViolationCase.save()
    rightsViolationCase = RightsViolationCase(id=79, name="Экономическое давление с целью заставить искать работу по найму",
                                              rightsViolation=rightsViolation)
    rightsViolationCase.save()
    rightsViolationCase = RightsViolationCase(id=80, name="Введение ограничений добровольного перехода в иные виды занятости или районы (косвенное принуждение к работе в определенных отраслях или районах)",
                                              rightsViolation=rightsViolation)
    rightsViolationCase.save()

    rightsViolation = RightsViolation(id=34,
                                      name="Нарушения при использовании принудительного (обязательного) труда в допустимых случаях (Конвенция МОТ №29 Относительно принудительного или обязательного труда)",
                                      groupOfRights=groupOfRights)
    rightsViolation.save()
    rightsViolationCase = RightsViolationCase(id=81, name="Привлечение к принудительному (обязательному) труду в ситуации, когда отсутствуют условия, позволяющие использовать принудительный труд",
                                              rightsViolation=rightsViolation)
    rightsViolationCase.save()
    rightsViolationCase = RightsViolationCase(id=82, name="Привлечение к принудительному труду лиц запрещенных категорий",
                                              rightsViolation=rightsViolation)
    rightsViolationCase.save()
    rightsViolationCase = RightsViolationCase(id=83, name="Несоблюдение ограничений при привлечении к принудительному (обязательному труду)",
                                              rightsViolation=rightsViolation)
    rightsViolationCase.save()
    rightsViolationCase = RightsViolationCase(id=84, name="Нарушения при оплате принудительного (обязательного) труда",
                                              rightsViolation=rightsViolation)
    rightsViolationCase.save()
    rightsViolationCase = RightsViolationCase(id=85, name="Нарушения при несчастных случаях и профзаболеваниях лиц, привлекавшихся к принудительному труду",
                                              rightsViolation=rightsViolation)
    rightsViolationCase.save()
    rightsViolationCase = RightsViolationCase(id=86, name="Нарушения в сфере охраны труда (здоровье и безопасность)",
                                              rightsViolation=rightsViolation)
    rightsViolationCase.save()
    rightsViolationCase = RightsViolationCase(id=87, name="Нарушения при привлечении к строительным или ремонтным работам на длительное время",
                                              rightsViolation=rightsViolation)
    rightsViolationCase.save()
    rightsViolationCase = RightsViolationCase(id=88, name="Нарушения при привлечении к принудительному труду для перевозки лиц или грузов в отсутствие изданной регламентации",
                                              rightsViolation=rightsViolation)
    rightsViolationCase.save()
    rightsViolationCase = RightsViolationCase(id=89, name="Нарушения при привлечении к принудительной обработке земли",
                                              rightsViolation=rightsViolation)
    rightsViolationCase.save()

    rightsViolation = RightsViolation(id=35,
                                      name="Нарушения, связанные с непринятием государством системных мер",
                                      groupOfRights=groupOfRights)
    rightsViolation.save()
    rightsViolationCase = RightsViolationCase(id=90, name="Отсутствие полной регламентации применения принудительного или обязательного труда государством",
                                              rightsViolation=rightsViolation)
    rightsViolationCase.save()
    rightsViolationCase = RightsViolationCase(id=91, name="Отсутствие возможности у трудящихся предъявлять претензии по поводу их привлечения к принудительному труду и / или отсутствие гарантий рассмотрения и учета претензий",
                                              rightsViolation=rightsViolation)
    rightsViolationCase.save()
    rightsViolationCase = RightsViolationCase(id=92, name="Необеспечение строгого соблюдения правил использования принудительного труда, в частности отсутствие компетентного органа надзора",
                                              rightsViolation=rightsViolation)
    rightsViolationCase.save()
    rightsViolationCase = RightsViolationCase(id=93, name="Необеспечение уголовного преследования лиц, незаконно использующих принудительный труд",
                                              rightsViolation=rightsViolation)
    rightsViolationCase.save()
    rightsViolationCase = RightsViolationCase(id=94, name="Непринятие мер, предусмотренных в Рекомендации, МОТ № 203",
                                              rightsViolation=rightsViolation)
    rightsViolationCase.save()

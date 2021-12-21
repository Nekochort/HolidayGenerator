from colorama import init, Fore, Back, Style
# init()
init(autoreset = True)
def congrats():
    from random import randint
    congr = ['Днём Рождения', 'Новым годом', 'Рождеством', 'Днём заповедников и национальных парков',
                 'Днём работника прокуратуры', 'Днём российской печати', 'Старым Новым годом', 'Крещением Господне',
                 'Днём инженерных войск в России', 'Днём студентов', 'Днём воинской славы России', 'Днём бармена',
                 'Масленицей', 'Днём российской науки', 'Международным днём стоматолога',
                 'Днём рождения гражданского воздушного флота в России', 'Днём дипломатического работника',
                 'Днём Святого Валентина', 'последним Днём Масленицы', 'Днём транспортной милиции России',
                 'Международным днём родного языка', 'Днём защитника Отечества', 'Днём эксперта-криминалиста МВД',
                 'Всемирным Днём гражданской обороны', 'Международным женским днём', 'Днём работника архивов',
                 'Днём работников органов наркоконтроля',
                 'Днём работников уголовно-исполнительной системы Министерства юстиции России',
                 'Днём работников геодезии и картографии',
                 'Днём образования подразделений экономической безопасности в МВД России', 'Днём моряка-подводника',
                 'Днём работников торговли', 'Днём работников гидрометеорологической службы России',
                 'Днём работника культуры России', 'Днём внутренних войск МВД России',
                 'Днём специалиста юридической службы в Вооруженных Силах', 'Днём смех',
                 'Днём единения народов Белоруссии и России', 'Пасхой', 'Днём геолога',
                 'Днём работника следственных органов', 'Днём рождения Рунета', 'Днём войск противовоздушной обороны',
                 'Всемирным днём авиации и космонавтики', 'Днём специалиста по радиоэлектронной борьбе',
                 'Всемирным днём интеллектуальной собственности', 'Всемирным днём охраны труда', 'Днём пожарной охраны',
                 'Праздником труда', 'Днём шифровальщика', 'Днём водолаза', 'Днём святого Георгия Победоносца',
                 'Днём радио', 'Днём Черноморского флота', 'Днём фрилансера', 'Международным днём музеев',
                 'Днём Балтийского флота', 'Всемирным днём метрологии', 'Днём Тихоокеанского флота',
                 'Днём военного переводчика', 'Днём кадровика', 'Днём славянской письменности и культуры',
                 'Днём филолога', 'Днём российского предпринимательства', 'Днём библиотекаря', 'Днём пограничника',
                 'Днём военного автомобилиста', 'Днём ветеранов таможенной службы', 'Днём химика',
                 'Днём российской адвокатуры', 'Международным днём защиты детей', 'Днём Северного флота России',
                 'Днём эколога', 'Днём социального работника', 'Днём независимости России', 'Днём пивовара',
                 'Днём мебельщика', 'Днём работников легкой промышленности', 'Днём работников миграционной службы',
                 'Днём медицинского работника', 'Днём кинологических подразделений МВД России',
                 'Днём дружбы и единения славян', 'Днём изобретателя и рационализатора', 'Днём молодежи России',
                 'Днём ГАИ', 'Днём работников морского и речного флота', 'Всероссийским днём семьи, любви и верности',
                 'Днём рыбака', 'Днём российской почты', 'Днём рождения морской авиации ВМФ России', 'Днём металлурга',
                 'Днём военно-морского флота', 'Днём парашютиста', 'Днём PR-специалиста',
                 'Днём системного администратора', 'Днём тыла вооруженных сил РФ',
                 'профессиональным праздником сотрудников инкассации', 'Днём железнодорожника',
                 'Днём воздушно-десантных войск', 'Днём железнодорожных войск', 'Днём строителя',
                 'Днём Военно-воздушных сил', 'Днём физкультурника', 'Днём Воздушного флота России', 'Днём археолога',
                 'Днём Государственного флага Российской Федерации', 'Днём российского кино', 'Днём шахтера в России',
                 'Днём знаний', 'Днём российской гвардии', 'Днём солидарности в борьбе с терроризмом',
                 'Днём специалиста по ядерному обеспечению',
                 'Днём работников нефтяной, газовой и топливной промышленности', 'Днём финансиста России',
                 'Днём тестировщика', 'Днём воинской славы России', 'Днём танкиста в России 2010', 'Днём Байкала',
                 'Днём секретаря', 'Днём работника леса', 'Днём рекрутера', 'Днём машиностроителя',
                 'Днём воспитателя и всех дошкольных работников', 'Днём работника атомной промышленности',
                 'Днём интернета в России', 'Международным днём пожилых людей в России', 'Днём сухопутных войск РФ',
                 'Днём ОМОНа', 'Днём Космических войск', 'Днём гражданской обороны МЧС России', 'Днём учителя',
                 'Днём работников уголовного розыска', 'Днём российского страховщика',
                 'Днём образования штабных подразделений МВД РФ',
                 'Днём командира надводного, подводного и воздушного корабля',
                 'Днём работника сельского хозяйства и перерабатывающей промышленности',
                 'Днём создания адресно-справочной службы Российского государства', 'Всемирным днём анестезиолога',
                 'Днём работников пищевой промышленности', 'Днём работников дорожного хозяйства',
                 'Днём рождения Российского военно-морского флота', 'Днём военного связиста',
                 'Литературным праздником «Белые журавли»', 'Днём работников рекламы',
                 'Днём подразделений специального назначения', 'Днём таможенника Российской Федерации',
                 'Днём работника кабельной промышленности', 'Днём создания армейской авиации России',
                 'Днём работников службы вневедомственной охраны МВД', 'Днём инженера-механика', 'Днём автомобилиста ',
                 'Днём сурдопереводчика', 'Днём судебного пристава', 'Днём судебного пристава',
                 'Днём народного единства', 'Днём военного разведчика', 'Всемирным днём мужчин',
                 'Международным днём КВН', 'Днём российской милиции', 'Всемирным днём качества',
                 'Днём работников Сбербанка России', 'Днём специалиста по безопасности',
                 'Днём войск радиационной, химической и биологической защиты', 'Днём социолога',
                 'Днём создания подразделений по борьбе с организованной преступностью',
                 'Всероссийский днём призывника', 'Днём участкового', 'Днём рождения Деда Мороза',
                 'Днём ракетных войск и артиллерии', 'Днём работника стекольной промышленности',
                 'Днём бухгалтера России', 'Днём работника налоговых органов РФ', 'Днём психолога в России',
                 'Днём морской пехоты', 'Днём оценщика в России', 'Днём матери в России',
                 'Всемирным днём борьбы со СПИДом', 'Днём банковского работника России', 'Днём юриста в России',
                 'Днём информатики в России', 'Днём сетевика в России', 'Днём образования российского казначейства',
                 'Днём Героев Отечества в России', 'Днём создания службы связи МВД России',
                 'Днём Конституции Российской Федерации', 'Днём Ракетных войск стратегического назначения',
                 'Днём подразделений собственной безопасности органов внутренних дел РФ',
                 'Днём работников органов ЗАГСа', 'Днём риэлтора',
                 'Днём работника органов государственной безопасности РФ', 'Днём энергетика',
                 'Днём дальней авиации ВВС России', 'Днём спасателя в России', 'Хэлоуином']
    print(Back.CYAN + Fore.BLACK + "С " + congr[randint(0, len(congr) - 1)] + "!")

print(Back.WHITE + Fore.BLACK + 'Добро пожаловать в генератор поздравлений "Хванессо"!')
print(Back.GREEN + Fore.BLACK + 'Разработчик: Nekochort')
print(Back.MAGENTA + Fore.WHITE + 'Автор идеи: alicehwan')
print(Back.YELLOW + Fore.BLACK + 'Дизайнер: Sonchous')
print("")

congrats()
while True:
    print(Back.WHITE + Fore.BLACK + 'Сгенерировать ещё? [да/нет]: ')
    answer = input()

    if answer == 'да':
        congrats()
    elif answer == 'нет':
        print(Back.WHITE + Fore.BLACK + "Для выхода нажмите любую клавишу...")
        input()
        break
    else:
        print(Back.RED + Fore.WHITE + "Написано ведь да/нет...Возвращайся, когда подумаешь над своим поведением...")
        print(Back.RED + Fore.WHITE + "Пока что нажми любую кнопку для выхода...")
        input()
        break

#Import everything from tkinter module
from tkinter import *

#To initialize Tkinter, we have to create a Tk root widget
#which is a window with a title bar
window = Tk()
window.title('Stock Market')
window.geometry('{}x{}'.format(1000, 1000))
window.wm_iconbitmap('icon.ico')

#so that a GUI object can be made that deals with all the visual side
class GUI:
    def __init__(self, window):

        #A Frame is a container widget which is placed inside a window,
        #which can have its own border and background
        #it is used to group related widgets together in an application’s layout.
        assets_frame = Frame(window,bg='cyan',width=200, height=1000, pady=3)
        graph_frame = Frame(window,bg='green',width=800, height=500, pady=3)
        company_frame = Frame(window,bg='red',width=800, height=200, pady=3)
        bank_frame = Frame(window,bg='orange',width=300, height=300, pady=3)
        news_frame = Frame(window,bg='blue',width=500, height=300, pady=3)

        #Layout of the main frames
        window.grid_rowconfigure(0, weight=1)
        window.grid_columnconfigure(0, weight=1)

        assets_frame.grid(column = 0,columnspan =2, rowspan = 10)
        graph_frame.grid(column =2, row= 0, rowspan = 4, columnspan = 8)
        company_frame.grid(column = 2,row = 5,rowspan = 2, columnspan = 8)
        news_frame.grid(column = 2, row =7, rowspan = 3, columnspan = 5)
        bank_frame.grid(column= 7, row = 7 , columnspan = 3 , rowspan = 3)

        #widgets for graph_frame
        graph_frame.pack_propagate(False)
        graph = Canvas(graph_frame, width=600, height=200,)
        graph.pack()
        # x values go left to right, y values go top to bottom
        # line drawn from (1,195) to (500,195)
        graph.create_line(1, 195, 500, 195, fill="black", width=3)

        #widgets for comapany_frame
        company_frame.grid_propagate(False)
        self.button = Button(company_frame,text = 'company', height = 10, width = 17)
        self.button.grid(column = 0, row = 0)
        self.button = Button(company_frame,text = 'company', height = 10, width = 17)
        self.button.grid(column = 1, row = 0)
        self.button = Button(company_frame,text = 'company', height = 10, width = 17)
        self.button.grid(column = 2, row = 0)
        self.button = Button(company_frame,text = 'company', height = 10, width = 17)
        self.button.grid(column = 3, row = 0)
        self.button = Button(company_frame,text = 'company', height = 10, width = 17)
        self.button.grid(column = 4, row = 0)
        self.button = Button(company_frame,text = 'company', height = 10, width = 17)
        self.button.grid(column = 5, row = 0)

        #widgets for assets_frame
        #Adding a scroll Bar the the assets frame
        assets_frame.pack_propagate(False)
        Scroll_assets = Scrollbar(assets_frame)
        Textbox = Text(assets_frame)
        Scroll_assets.pack(side=RIGHT, fill=Y)
        Textbox.pack(side=LEFT, fill=Y)
        Scroll_assets.config(command=Textbox.yview)
        Textbox.config(yscrollcommand=Scroll_assets.set)
        quote = ('BeeMovieScriptAccordingtoallknownlawsofaviationthereisnowayabeeshouldbeabletoflyItswingsaretoosmalltogetitsfatlittlebodyoffthegroundThebeeofcoursefliesanywaybecausebeesdontcarewhathumansthinkisimpossibleYellowblackYellowblackYellowblackYellowblackOohblackandyellowLetsshakeitupalittleBarryBreakfastisreadyOomingHangonasecondHelloBarryAdamOanyoubelievethisishappeningIcantIllpickyouupLookingsharpUsethestairsYourfatherpaidgoodmoneyforthoseSorryImexcitedHeresthegraduateWereveryproudofyousonAperfectreportcardallBsVeryproudMaIgotathinggoinghereYougotlintonyourfuzzOwThatsmeWavetousWellbeinrow118000ByeBarryItoldyoustopflyinginthehouseHeyAdamHeyBarryIsthatfuzzgelAlittleSpecialdaygraduationNeverthoughtIdmakeitThreedaysgradeschoolthreedayshighschoolThosewereawkwardThreedayscollegeImgladItookadayandhitchhikedaroundthehiveYoudidcomebackdifferentHiBarryArtiegrowingamustacheLooksgoodHearaboutFrankieYeahYougoingtothefuneralNoImnotgoingEverybodyknowsstingsomeoneyoudieDontwasteitonasquirrelSuchahotheadIguesshecouldhavejustgottenoutofthewayIlovethisincorporatinganamusementparkintoourdayThatswhywedontneedvacationsBoyquiteabitofpompunderthecircumstancesWellAdamtodaywearemenWeareBeemenAmenHallelujahStudentsfacultydistinguishedbeespleasewelcomeDeanBuzzwellWelcomeNewHiveOitygraduatingclassof915ThatconcludesourceremoniesAndbeginsyourcareeratHonexIndustriesWillwepickourjobtodayIhearditsjustorientationHeadsupHerewegoKeepyourhandsandantennasinsidethetramatalltimesWonderwhatitllbelikeAlittlescaryWelcometoHonexadivisionofHonescoandapartoftheHexagonGroupThisisitWowWowWeknowthatyouasabeehaveworkedyourwholelifetogettothepointwhereyoucanworkforyourwholelifeHoneybeginswhenourvaliantPollenJocksbringthenectartothehiveOurtopsecretformulaisautomaticallycolorcorrectedscentadjustedandbubblecontouredintothissoothingsweetsyrupwithitsdistinctivegoldenglowyouknowasHoneyThatgirlwashotShesmycousinSheisYeswereallcousinsRightYourerightAtHonexweconstantlystrivetoimproveeveryaspectofbeeexistenceThesebeesarestresstestinganewhelmettechnologyWhatdoyouthinkhemakesNotenoughHerewehaveourlatestadvancementtheKrelmanWhatdoesthatdoOatchesthatlittlestrandofhoneythathangsafteryoupouritSavesusmillionsOananyoneworkontheKrelmanOfcourseMostbeejobsaresmallonesButbeesknowthateverysmalljobifitsdonewellmeansalotButchoosecarefullybecauseyoullstayinthejobyoupickfortherestofyourlifeThesamejobtherestofyourlifeIdidntknowthatWhatsthedifferenceYoullbehappytoknowthatbeesasaspecieshaventhadonedayoffin27millionyearsSoyoulljustworkustodeathWellsuretryWowThatblewmymindWhatsthedifferenceHowcanyousaythatOnejobforeverThatsaninsanechoicetohavetomakeImrelievedNowweonlyhavetomakeonedecisioninlifeButAdamhowcouldtheyneverhavetoldusthatWhywouldyouquestionanythingWerebeesWerethemostperfectlyfunctioningsocietyonEarthYoueverthinkmaybethingsworkalittletoowellhereLikewhatGivemeoneexampleIdontknowButyouknowwhatImtalkingaboutPleaseclearthegateRoyalNectarForceonapproachWaitasecondOheckitoutHeythosearePollenJocksWowIveneverseenthemthiscloseTheyknowwhatitslikeoutsidethehiveYeahbutsomedontcomebackHeyJocksHiJocksYouguysdidgreatYouremonstersYoureskyfreaksIloveitIloveitIwonderwheretheywereIdontknowTheirdaysnotplannedOutsidethehiveflyingwhoknowswheredoingwhoknowswhatYoucantjustdecidetobeaPollenJockYouhavetobebredforthatRightLookThatsmorepollenthanyouandIwillseeinalifetimeItsjustastatussymbolBeesmaketoomuchofitPerhapsUnlessyourewearingitandtheladiesseeyouwearingitThoseladiesArenttheyourcousinstooDistantDistantLookatthesetwoOoupleofHiveHarrysLetshavefunwiththemItmustbedangerousbeingaPollenJockYeahOnceabearpinnedmeagainstamushroomHehadapawonmythroatandwiththeotherhewasslappingmeOhmyIneverthoughtIdknockhimoutWhatwereyoudoingduringthisTryingtoalerttheauthoritiesIcanautographthatAlittlegustyouttheretodaywasntitcomradesYeahGustyWerehittingasunflowerpatchsixmilesfromheretomorrowSixmileshuh')
        Textbox.insert(END, quote)

        #widgets for news_frame       
        news_frame.pack_propagate(False)
        c = Canvas(news_frame)
        c.pack(expand=YES,fill=BOTH)
        c.background = PhotoImage(file='woop.gif')
        c.create_image(0,0,image=c.background,anchor='nw')
              
gui = GUI(window)
window.mainloop()

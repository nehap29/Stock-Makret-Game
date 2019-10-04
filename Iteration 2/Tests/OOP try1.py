
import tkinter as TK

#################################################################################


#GUI CLASS


#################################################################################


class GUI(TK.Tk):
    def __init__(self,app,*args,**kwargs):
        TK.Tk.__init__(self, *args, **kwargs) # makes 'self' the root TK window
        self.app = app
        self.title('Stock Market')
        self.geometry('{}x{}'.format(1000, 1000))
        self.wm_iconbitmap('icon.ico')
        self.assets= Assets(app, self)
        self.assets.pack(side=TK.LEFT,fill=TK.Y)

        
    def start(self):
        self.mainloop()

class GUIBox(TK.Frame):
    def __init__(self, app, parent, *args, **kwargs):
        TK.Frame.__init__(self, parent, *args, **kwargs)
        self.app = app
        self.parent = parent
        self.make_widget()

        
class Assets(GUIBox):
    def make_widget(self):
                Scroll_assets = Scrollbar(self)
                Textbox = Text(self,bg='#0a561b',width=200, height=1000, pady=3,highlightthickness=4, highlightbackground="#111")
                Scroll_assets.pack(side=RIGHT, fill=Y)
                Textbox.pack(side=LEFT, fill=Y, padx=5, pady=5)
                Scroll_assets.config(command=Textbox.yview)
                Textbox.config(yscrollcommand=Scroll_assets.set)
                quote = ('BeeMovieScriptAccordingtoallknownlawsofaviationthereisnowayabeeshouldbeabletoflyItswingsaretoosmalltogetitsfatlittlebodyoffthegroundThebeeofcoursefliesanywaybecausebeesdontcarewhathumansthinkisimpossibleYellowblackYellowblackYellowblackYellowblackOohblackandyellowLetsshakeitupalittleBarryBreakfastisreadyOomingHangonasecondHelloBarryAdamOanyoubelievethisishappeningIcantIllpickyouupLookingsharpUsethestairsYourfatherpaidgoodmoneyforthoseSorryImexcitedHeresthegraduateWereveryproudofyousonAperfectreportcardallBsVeryproudMaIgotathinggoinghereYougotlintonyourfuzzOwThatsmeWavetousWellbeinrow118000ByeBarryItoldyoustopflyinginthehouseHeyAdamHeyBarryIsthatfuzzgelAlittleSpecialdaygraduationNeverthoughtIdmakeitThreedaysgradeschoolthreedayshighschoolThosewereawkwardThreedayscollegeImgladItookadayandhitchhikedaroundthehiveYoudidcomebackdifferentHiBarryArtiegrowingamustacheLooksgoodHearaboutFrankieYeahYougoingtothefuneralNoImnotgoingEverybodyknowsstingsomeoneyoudieDontwasteitonasquirrelSuchahotheadIguesshecouldhavejustgottenoutofthewayIlovethisincorporatinganamusementparkintoourdayThatswhywedontneedvacationsBoyquiteabitofpompunderthecircumstancesWellAdamtodaywearemenWeareBeemenAmenHallelujahStudentsfacultydistinguishedbeespleasewelcomeDeanBuzzwellWelcomeNewHiveOitygraduatingclassof915ThatconcludesourceremoniesAndbeginsyourcareeratHonexIndustriesWillwepickourjobtodayIhearditsjustorientationHeadsupHerewegoKeepyourhandsandantennasinsidethetramatalltimesWonderwhatitllbelikeAlittlescaryWelcometoHonexadivisionofHonescoandapartoftheHexagonGroupThisisitWowWowWeknowthatyouasabeehaveworkedyourwholelifetogettothepointwhereyoucanworkforyourwholelifeHoneybeginswhenourvaliantPollenJocksbringthenectartothehiveOurtopsecretformulaisautomaticallycolorcorrectedscentadjustedandbubblecontouredintothissoothingsweetsyrupwithitsdistinctivegoldenglowyouknowasHoneyThatgirlwashotShesmycousinSheisYeswereallcousinsRightYourerightAtHonexweconstantlystrivetoimproveeveryaspectofbeeexistenceThesebeesarestresstestinganewhelmettechnologyWhatdoyouthinkhemakesNotenoughHerewehaveourlatestadvancementtheKrelmanWhatdoesthatdoOatchesthatlittlestrandofhoneythathangsafteryoupouritSavesusmillionsOananyoneworkontheKrelmanOfcourseMostbeejobsaresmallonesButbeesknowthateverysmalljobifitsdonewellmeansalotButchoosecarefullybecauseyoullstayinthejobyoupickfortherestofyourlifeThesamejobtherestofyourlifeIdidntknowthatWhatsthedifferenceYoullbehappytoknowthatbeesasaspecieshaventhadonedayoffin27millionyearsSoyoulljustworkustodeathWellsuretryWowThatblewmymindWhatsthedifferenceHowcanyousaythatOnejobforeverThatsaninsanechoicetohavetomakeImrelievedNowweonlyhavetomakeonedecisioninlifeButAdamhowcouldtheyneverhavetoldusthatWhywouldyouquestionanythingWerebeesWerethemostperfectlyfunctioningsocietyonEarthYoueverthinkmaybethingsworkalittletoowellhereLikewhatGivemeoneexampleIdontknowButyouknowwhatImtalkingaboutPleaseclearthegateRoyalNectarForceonapproachWaitasecondOheckitoutHeythosearePollenJocksWowIveneverseenthemthiscloseTheyknowwhatitslikeoutsidethehiveYeahbutsomedontcomebackHeyJocksHiJocksYouguysdidgreatYouremonstersYoureskyfreaksIloveitIloveitIwonderwheretheywereIdontknowTheirdaysnotplannedOutsidethehiveflyingwhoknowswheredoingwhoknowswhatYoucantjustdecidetobeaPollenJockYouhavetobebredforthatRightLookThatsmorepollenthanyouandIwillseeinalifetimeItsjustastatussymbolBeesmaketoomuchofitPerhapsUnlessyourewearingitandtheladiesseeyouwearingitThoseladiesArenttheyourcousinstooDistantDistantLookatthesetwoOoupleofHiveHarrysLetshavefunwiththemItmustbedangerousbeingaPollenJockYeahOnceabearpinnedmeagainstamushroomHehadapawonmythroatandwiththeotherhewasslappingmeOhmyIneverthoughtIdknockhimoutWhatwereyoudoingduringthisTryingtoalerttheauthoritiesIcanautographthatAlittlegustyouttheretodaywasntitcomradesYeahGustyWerehittingasunflowerpatchsixmilesfromheretomorrowSixmileshuh')
                Textbox.insert(END, quote)


class CLMCApp():
    
    def __init__(self):
        self.gui = GUI(self)

    def run(self):
        self.gui.start()

app = CLMCApp()
app.run()

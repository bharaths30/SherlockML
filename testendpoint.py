import MySQLdb
req_json={"gpsDataObject":{"latitude":111.23,"longitude": -123.45, "cityName":"Tempe"},"id":"bsuresh@asu.edu","oneDataPoint":[6.87253133515609, 1.087371209127621, -5.152202019774421, -0.2519499741185456, -1.0610277645016595, -1.4317820096679696, 6.96591517610706, 6.702510743408844, -3.976627199012343, -9.906681940271579, 0.38841300830686976, 8.025094493777875, -4.857890824607547, 8.021359623515615, -4.015784676708045, 1.4546889801897471, -0.9064198135814792, 0.8373661226039921, -1.3170497131354324, -7.843911167071987, 3.54524040119154, 3.081775514469241, -8.970307777255467, -6.264829282975146, 9.52506056742692, -8.433922107151734, -9.568150643051256, -9.297074729248695, -2.2360544627959644, 0.963527826683297, 3.0301551111981144, 3.4993637379684284, -2.6412715298766027, -1.4405765469274083, -4.7529231435550585, 8.256615271328059, 8.8866071089397, -0.15162072394774917, -7.40175462609975, -2.487236023375285, 5.776070115481835, -8.693119238114107, 6.453720960916762, -4.904221343971466, -0.46740999314422993, 4.030590048767168, -1.9749791342685779, 0.6493734257294133, 7.000208683790689, -6.029910779222137, 2.3725245210702113, 5.657238865956284, 2.2203447134345318, 2.2693167746895995, 9.241753555572949, 7.104060155809318, -4.636869206985632, -2.7447364067726614, 4.440462935884554, 7.745987250890572, -7.476819098388498, -8.890584448740169, -6.0264328881025975, 8.518024775628586, 2.1576745073827635, 4.657628277393737, -6.791566215883453, 8.648191375602131, 0.3638762151498085, -2.9194551824536497, -0.2532694655683514, -7.184484094634255, -2.418765208271636, -8.768282568749648, 0.3374497673410666, -6.0227589859838275, -6.632046558726716, -0.223766848512712, 0.6074808258573317, 8.352524534745442, -0.17649211371905338, 3.863595009006719, 4.277603904974885, 1.4324455232015971, -4.2261546669749395, -7.616562929446815, -4.112519187259387, -9.971728741463199, 6.829929829300475, 9.573889583265295, 9.236680134188944, 5.3836290804313, -0.3405089632402074, 2.499719745234202, 8.68463530116906, 7.83131471746934, 3.436699214719251, -1.5241991207796133, -2.7913228500793297, -6.987727984036223, -6.09335895984546, -4.0165608869991605, 6.789784230275892, 0.9587958920548356, -0.17951823851483972, 2.857704067908781, 0.39830412046926966, -5.795749110334889, -9.693694825560337, 9.2529426918776, 3.0439656098363947, 4.180158895632255, -4.665557894666699, 7.321145094339634, 1.8397509826411564, -7.814878988722782, 3.424090543936206, -8.95840039150901, -8.363339309946126, -0.9518624399019782, 4.940511615117039, -7.72994788998507, -3.4932623650291683, 0.4894080542959838, 7.792885625074518, 7.41179901813269, -4.236197631660168, -9.523954559269578, -6.7164171178336085, -0.7864897966785485, 3.1645488609146284, -5.985104295129002, -2.192008961704235, -8.799323305063488, -9.663192585086708, -8.909220137288498, 7.327553884751204, 7.985777813061951, -5.359060285174257, 0.17675957161285005, -0.9968181351262206, 0.9156937513030705, -6.057400346519217, 7.880136353277614, -0.16355787995583526, 2.251143294551749, -9.215593508344021, 6.351487823533798, 0.4990439811634815, 9.536395796545232, -3.547006311778267, 5.2146431375121125, 5.204066837580054, 7.737752795746935, 4.735625790521095, 2.2406954799279806, -8.892181653356454, -2.7258200159325474, 7.499807077885809, -7.664646571265317, -6.271546751739279, 0.309863971285262, -8.487515363585796, 8.980255420368689, 2.765974234206631, 0.9705370708230916, -1.4988049762529787, 4.82462744090312, 3.6074679837840407, 3.0848520569885363, -7.04524646287525, 8.873933039440928, 2.9183553441488197, 3.7034037613163644, -4.180983455380387, -9.388427774408857, 9.681106147444837, -4.891920558816318, 7.838729250033637, 2.401620977864912, 8.533147422778924, -6.602345880093301, -5.608084075510275, -1.2837835824497574, -6.76235712922014, -5.1235009563145635, 2.30912444564896, -9.37662856367994, -8.569659214634047, -9.812485556665969, -0.24945008474839625, 9.736965028717442, 7.241437641825893, 3.5625145336546638, -2.2355247273932495, -7.164347983657288, 8.944998138330249, -6.781593648322377, 9.0704439800325, 6.918048358230738, 6.864071062172062, -3.501952334746308, -7.136346278547741, 9.2538479864183, 9.36997278558501, 8.75863166962058, 3.2149605524192726, 3.2326285932269894, 9.995506545727004, -9.369575736947272, 4.665151868204651, -2.3182394730991245, -7.733278647810867, 6.714435792265036, -1.1643562761130948, -6.707698315103263, 8.602052478516516, -1.8414279376593807, -2.4170444502131216, 1.3742170901743336, -2.435790442705801, -6.06187835324082, -9.764158204662799, -2.0336056063843166, -3.970537382105526, -8.500734985977825, -9.760081887127324, 7.359298156196687, 3.9640931445158536, 9.512930513454016, 7.841618481562204, 7.165818543249198, -4.417183151215383, 3.151426215007014, -9.78467423131659, 8.043365335821036, -9.223635454773065, 3.60959305167448, -2.060001772781776, -0.24686404771116877, 6.546262080286411, -1.7893076447821663, 6.4874705556756425, -7.735784902996405, 6.29295530571407, -6.949287405305398, 0.45272385134482107, -6.716034567703996, -4.267649186167111, -5.512541610783739, 4.172272949429098, -0.23823664821105162, -9.662821531436478, -7.471128879381919, -1.1827245346576358, 6.609770596685305, 9.272352828081118, -5.030073877195342, -7.544221731299765, -3.80287362430842, -8.017119968261566, 6.629766286915643, -9.408292481538826, 8.980896492704712, 2.5321738701971412, -7.722756256882201, -7.688293646906348, 1.1222185888670708, -0.1907023580893643, 0.5956776783264228, 1.7516119049051753, -3.2120565664097445, -5.1982129646050845, -9.134811377471712, 9.650409765636073, 1.4763711371876038, 5.113624806309048, 4.596589721555905, -3.145052348611923, 2.8790900161916326, 3.312934171013042, -3.0068398126713074, 3.626847497328999, 1.3104493867325715, 6.928585428599703, 3.5691284228126126, -8.085827493225757, 4.653832025396188, -2.837125962206713, -8.796803857023514, -4.086334323742098, -4.780031742182597, 4.3471701011801205, -4.436614817653504, -9.766185052919234, -3.918504857326937, 9.757648665178774, 5.655369774598755, 9.213315583022165, 5.589127133397591, 8.540698552575329, -7.543711180206703, -4.833461264638981, 3.469804368154321, 7.090434796674426, -4.582519555685744, 4.560590269210055, -2.1572497857463606, 0.9879282205294704, 3.0218216855057953, 4.432688745697057, -7.3836704329030916, 9.038386203307589, 3.5295090267651332, 8.982785848501951, -3.6937210301931884, 7.210273746399238, 1.8142874327143907, -7.007199310089655, -1.187565539879694, 7.585914905647083, 2.766278775455593, -9.919620131043668, -5.821520718266758, 3.9255812690748186, 9.194592100497847, -1.0579276064385148, -0.6540397287162811, 7.17802545291644, -1.7760285910565248, 9.904857868549847, 5.2316366295635515, 7.633828022461042, -9.044277335431438, 0.06353122949474255, -5.938795306005053, 0.7299791786075147, -8.080787802958191, 4.400198891580038, 0.22320060529591146, -1.11719034617275, 2.6337705088318746, 8.665706965128809, 3.7643625047520324, -8.60449703402159, -4.030050987374263, -6.418027156944226, -6.7646053035274, 0.27590955713109544, 2.1372638089130973, 3.586700397003055, 8.131109730097087, -4.864681966360553, -2.077342372248589, 6.257373585126619, 3.088521792749834, 3.3514620051738646, 0.1381846358501555, 5.413405438446151, 5.360799310077164, 4.055308212999476, 1.5127760194626632, 5.959336951243246, -0.5882915562646964, 6.189045911319685, -0.34213284692168955, 7.032713288118867, -4.020769397379597, 3.2655041216580223, -8.001335930521174, -2.672410940647394, 9.923707275658359, -1.3082201348467688, -4.056525050317477, -7.149938897245265, 5.912355947961668, 9.179401655267554, 1.2057515681468125, 8.746732196592877, 8.42014501878834, -7.0556887752648905, -3.4752905432095, 7.821858179576896, -4.77043513711227, 5.3582446016337, -6.7569953571422285, 6.724610313729208, -5.915438040593221, 6.136865498549639, 2.141076567600548, 8.967409705620302, -0.9849451851133963, 1.7397775621519163, 9.095735293983477, 7.410131875744838, -5.046093096110617, -8.304658035592428, 6.05788292890718, 4.830287956050256, 2.7879321153656296, -7.862663083945451, 9.355706560806038, -7.135797923670553, 5.6897379222212745, -1.5497236764548568, -6.459087744898733, 9.963401063979262, -0.8310575764618893, -0.3242877760183944, -6.790544492885546, -3.766971223371103, -0.8238765864543218, -3.6518804108583547, 9.500128251242419, 6.027034935504243, 0.4214933742206046, -7.012380483174736, 3.4892739687270513, 9.940379122681396, -7.680526105083317, 6.462331761589478, -8.585573357893256, -4.242579745750847, 2.7720603710523672, 0.7496485091864287, 2.938804770063282, -2.2839995349051945, 2.326671662120713, 7.624816813975148, -0.8275235325397539, 5.26866912389548, -6.507799070215525, 1.052133389464366, -0.8756425688229612, 0.25899110191749486, -9.223620984943665, 1.019560860969257, -7.180202103439523, -8.526417366660716, -0.21501334337548705, -7.897725063344108, 2.876509618046237, 3.5562851151652097, -1.0485189050774117, -5.931508224977035, 2.742085559738854, 7.601496925067501, -6.834114574786763, -2.053626598883909, -7.900657759134124, 7.759715908277283, -8.05147765621025, -1.0845419950813806, -1.2836476965535581, -8.68253153443822, -6.603815759942617, -3.9846097651419887, -6.858494667538535, 2.7411801061973122, -6.455459313259791, -7.653575805692885, 9.014141502527671, -0.5801996254961388, -0.6858258204780316, -6.6829760785550585, -4.403596050881882, -5.688174688213634, -5.8921944436070355, -7.2861151513256335, -4.305454673946989, 3.7527759186248755, 5.864274406169693, 8.376315607131772, -4.880923957863132, -8.646868151753095, 9.958651169654654, 7.424129377417369, -9.161458525936899, -6.510572493413815, -5.254555453946668, 6.192084893149527, -7.363137131310662, 2.9099192170379453, 1.3512060918751896, -3.3103753828256144, 3.6209352275618336, -5.925553102857954, 1.1151572069472682, 5.828453928359599, -1.4634293610168605, -6.465059700799856, -5.058330442483507, -4.5645338215525015, 0.9091568173144537, -4.3540731107553405, 5.17995471255005, -7.766998271821437, 4.0795067050422595, -1.3812008186824958, 5.88086305250614, 2.9181717706963344, -0.24452310065125538, 4.697438480754201, 8.066034652369048, -3.167169536351291, 7.870229614539124, -9.513129580066245, -3.2669710371488225, 9.577485586371711, 3.4131556420531517, 2.8740329494494343, -0.8417348908381062, 1.4935382347796011, -9.497593259857497, -9.119210403828117, -8.091127703835369, -8.296021790660664, 1.7643204888948976, -8.439659283258298, 3.9760673579716475, -1.2269080951836955, 7.417637331115287, 2.0355447199068024, -4.711645079349522, -6.469025253411735, 8.218918601029849, 2.2158304122219903, -0.12419631561575173, 9.88205115068287, -2.8886172831309302, 1.7170809250723273, 3.639792634152162, -0.5148887437526213, -8.612341051194548, 4.4968639775902925, -8.153061504084992, -7.701442470706581, 6.817919663910313, -5.233872829153158, -6.335134817727182, -7.68171757088107, 9.533521051455075, 3.370927180879379, 6.197223233493734, 4.50230692999445, 7.256139818951976, 4.350279427000579, 7.812484506136585, -6.43948610582969, 9.216450500179644, -1.7200389849602775, 2.842093070221166, 3.667439643396717, -8.298963342016506, 2.12131685410216, 8.735946924787712, -9.54335819987746, -0.4196971524464015, 1.162986716366742, 1.2358788003815935, 5.87466616923928, -9.347966124973501, 8.257905630198277, 2.305835705149855, 8.73460538804395, 9.22109535054448, -5.2838603961955855, -3.478064418524953, 7.068492670435507, 6.024074901463543, 3.5322576988802528, -5.630280268024599, -6.795251593055074, 1.1870625599362779, 9.531065447681897, 7.8874019151634265, -6.951863285055264, -1.0971162948466677, -8.040145059515423, 6.680885446984135, 6.153814077549853, -5.834947139268342, 7.510931934367854, -3.9299409351330805, -5.932197614010302, 9.173584404258115, 4.8734352636477, 8.125018978407176, 7.2123804640584375, -0.24132188476659522, -6.320720040556351, -5.940458816814984, 5.746081520341697, -4.548935768105647, 5.30731836587486, -5.2948409830079886, -0.31909112411592844, -8.80838337883749, 5.6105452069199835, 3.5957139623167063, 9.568143698361894, -0.5238709426413486, -9.950618527588572, 8.722414111304232, 3.167017410337243, 5.970718608750687, 0.32513294386065184, -7.5389465318835525, -4.478739426409701, 9.15770820393853, -7.954386575639347, -7.473321999754649, -9.126759949027507, 4.295162405834169, -6.193992064713958, -4.043878652466615, 7.4117634226015525, 1.3082782181663184, 4.702447851572465, 0.5330823987390687, 3.7760013518482367, 9.941468639672422, 7.686589753886047, -9.689185146633852, -3.2724547791670116, -1.047941418647989, 5.145485169744667, 8.999647585929175, 0.6358566796737453, -4.288624759248661, -4.8404107948763, -9.465240979957379, 1.4759096135898258, 9.653012317415516, -4.83150414329526, -1.991966785618665, -2.9838667532655823, 4.4072185516301445, 4.457181499470757, 0.47540483247618326, 6.818604231108029, -7.689717414166446, 5.228696962091821, -5.429968420304043, 2.1743661610035474, -3.9487220836592973, -4.041772555541677, -1.9707873346000468, -5.171924463561403, -9.830960509176363, -0.3895501808357089, 8.094514474583029, 2.3659430744557817, 1.1571268469527052, 7.561641237273534, 7.386214398034731, 6.5187207671495315, -4.619423879101299, -1.1565764037267598, 3.539890449463609, -7.240008254846682, -1.0910137950483527, -1.2561145307636679, -9.150214528907657, -2.249228679981652, -3.7566223479208727, -0.7617148515213366, -5.768740440567117, 0.9056842185285667, 3.8786921555156297, 6.655648213184627, 5.308636751275724, 3.0691902074227713, 5.7304469364688195, -7.405374399581737, 3.633622838888508, -2.389965079327303, 7.294853793596886, -0.7114107128326381, -3.9404854270663403, 9.250495617189397, -1.2060565026345174, 6.124404794921745, -0.026208359545798032, -2.1083611697802107, 1.3524333165663176, 2.7046996422570153, -8.732055416764064, -0.1338998913136571, -0.4279299036873887, -6.669932792537785, -7.447076637347032, 4.232364142871701, 2.4565162674997616, -7.498072569498644, 8.163593211108381, -5.331656714790192, -8.609614024276508, -2.61343193259878, 3.2828686675682306, 0.6491014196772209, 4.697864915141096, 8.901659876450239, -3.8295141527559355, 5.977275879760871, 6.635636214904906, -6.099340858397182, 4.6991226760095905, 3.219318062074951, 9.445627717937825, -8.169278270053761, 1.14835369408752, -3.691459381237072, -3.2842834949768047, -2.9958100171795676, -0.7746806799581059, 4.873904045778749, -2.8397565244330885, 8.161190760972485, 2.273572956638967, 1.6349182270138307, -9.206842053802626, 0.053890403868592784, 7.309000565801341, 1.8985133218234793, -4.32855695359375, -2.365145904274071, -9.472034036575113, 5.85445063135683, -0.6880280618066248, -1.3018414591629366, 4.3959258168593, -4.520543206246865, 3.089460429266902, 7.916339363568014, -8.081033142912627, 3.133927235675829, 2.3821143091362433, 2.866571661767823, 2.552886853117025, 6.20999012443831, -4.561191389186467, 0.3744225912732997, 2.7297016108306877, 8.578009607576782, 8.139058234106386, -4.754554609190793, -7.229837896034694, -3.0180030598042666, 9.467737460402507, 0.8222951410178609, -6.4238886953032726, -5.40648162012753, -6.146508578808964, -2.9540216456790453, -1.4992742989399837, -8.103617977996041, -1.6773649651785423, -2.0189209475626146, 3.696004156805156, -4.602600881835743, 4.01497891382235, -5.352597818200295, 5.453382152264872, -5.510662842369614, -8.211544017774555, 7.196893531981022, -3.24905065368823, 7.444089057174814, -5.54667175884714, -7.992296185222565, 0.7243803585166937, 3.6794288549866323, -1.050387597707056, -8.305340363900342, -6.27375586096603, -7.313424498582581, 0.5912924918582707, -4.636892221964713, -2.86201345319101, 1.246189884322881, -1.5870330551162315, -7.8322992484141825, 1.5849843524319596, -2.8873009397818823, -5.7553931671788146, 3.325064825263926, 4.699241224017525, -6.1991719870179125, 0.5453444864691281, -6.819872282528124, 4.520471925877452, 6.953262945626193, 8.23445643210676, -1.368296947358882, 0.09289100046342647, -0.7733138027764035, 7.550273661118311, -4.518121328463485, 6.958680428747449, 3.357117681417069, -0.56519250432798, -7.073247731452543, -2.683975613559566, -4.1022084318116425, -0.8922328160677555, 4.885462989442429, -0.6885126570882001, -8.570162488293096, 4.199898051698007, 0.23857738477714463, 1.066388366226878, -8.03134090465575, -5.560493636495661, -5.953766719824536, 5.5993452172988345, 3.106198759885645, -2.374434648205983, -1.9210157734175013, -9.472575887948596, 2.8493982596336576, -6.638947390558987, -4.832814493189801, 5.940270072247223, 9.313880328672418, 6.859007341036886, 2.38829943174224, 2.606670745445186, 4.164003651901869, -7.123894535219586, 4.297172838142281, 4.440820578612662, -2.3362457411526254, 0.8206386006635942, -8.199514245029096, -2.2436794858479603, -9.352899617029259, 7.038072784493252, -3.3186541151413635, 1.9590845487346407, 4.960918881287473, -2.783603937131412, -6.073215172722842, -6.123234870393322, 9.558297838266832, -2.9329248051825036, -8.531512112283197, 1.1638429705447084, 0.6471552353960437, 9.152679142970626, 6.851698141849415, -6.300981744379397, 8.511987885753008, 9.528022622873479, -1.7182561327500085, 4.971441283691142, 7.613388970903117, -2.666466537962826, -9.579738174333079, 4.897684944080414, 7.499196704633373, -7.928513912486985, -6.984052396610467, 2.6546378845568963, -1.06266768990832, -1.8049985331501759, 9.571089606399596, -9.940819503254268, 8.438968226533742, -3.88013409086009, -1.6858014913217296, -9.28827877184186, 3.77840620145021, 1.838434391230571, 5.114653844570379, -3.6037146407439664, -0.4739167348943596, 9.08612017829271, -5.893550023676546, 6.132144939942265, -8.600921471213326, 3.9196643939289437, -1.646918121801912, -8.9992164581071, 1.2943260856509493, -6.686309834622164, 0.7478884856024237, 4.267614077868021, 0.9439352279272999, 5.4768795809307065, -8.331801263064193, -1.0831699827294798, 0.5811352965410226, -4.9390478187696445, -6.230239146181917, 6.79289556225115, -8.67934713911891, -6.828230096042603, -0.038526997994123846, -8.541339017045392]}

def traininginsert():
	#print req_json
	conn=MySQLdb.connect(user='root',passwd='GroupTen',db='sherlock')
    	cursor = conn.cursor()
	#req_json = request.get_json()
	dataPoint = req_json['oneDataPoint']
	emailID = req_json['id']
	gpsLocation = req_json['gpsDataObject']
	countQuery = "SELECT COUNT(*) FROM training_done where userId=\""+emailID+"\";"
	cursor.execute(countQuery)
	result={}
	if cursor.fetchone()[0]==0:
		insertQuery = "INSERT INTO training(latitude,longitude,city"
    		for i in range(0,300):
    	   		insertQuery=insertQuery+",x"+str(i+1)+",y"+str(i+1)+",z"+str(i+1)
    		insertQuery=insertQuery+",id) VALUES ("
    		insertQuery = insertQuery + str(gpsLocation['latitude'])+","+str(gpsLocation['longitude']) +",\""+str(gpsLocation['cityName'])+"\""
    		for eachVal in dataPoint:
    	   		insertQuery = insertQuery +","+str(eachVal)
    		insertQuery = insertQuery +",\""+emailID+"\");"
    		cursor.execute(insertQuery)
    		conn.commit()
    		#result = {}
    		result['insertSuccess']=True
    		result['trainingComplete']=False
    		result['anomaly']=False
    	else:
        	testDataSet=[]
        	testDataSet.append(dataPoint)
        	selectNameQuery="SELECT name FROM users WHERE email=\""+emailID+"\";"
        	g.cursor.execute(selectNameQuery)
        	name = g.cursor.fetchone()[0]
        	boolAnomoly=detect.detect(testDataSet,emailID,emailID,name,gpsLocation['latitude'],gpsLocation['longitude'],gpsLocation['cityName'])
        	#result={}
        	result['insertSuccess']=False
        	result['trainingComplete']=True
        	result['anomaly']=True
    	conn.close()
    	#data = json.dumps(result)
    	#resp = Response(data,status=200,mimetype='application/json')
    	return result

print traininginsert()

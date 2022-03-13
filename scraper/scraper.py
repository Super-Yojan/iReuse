import sys
import timeit
from dataclasses import replace
from pickletools import TAKEN_FROM_ARGUMENT4U
import sqlite3
import requests
from bs4 import BeautifulSoup

start = timeit.default_timer()

con = sqlite3.connect('test.db')
cur = con.cursor()
# Name of the file is going to be the first command line argument, the website is the second element passed in
url = sys.argv[1]

def scraper(url):
    keywords = ""
    keywords = ["recycle", "Recycle", "RECYCLE", "DIY", "diy",
                "reuse", "Reuse", "REUSE", "re-use", "Re-use", "RE-USE"]
    resp = requests.get(url).content
    soup = BeautifulSoup(resp, 'html.parser')
    temp = soup.find_all("p")
    commonObjects = {'clamp', 'shampoo', 'glow', 'dresses', 'balloon', 'buckle', 'stick', 'teddies', 'pot', 'fork', 'street', 'flag', 'liner', 'video', 'tooth', 'soda', 'sketch', 'magnet', 'band', 'milk', 'seat', 'white', 'helmet', 'puddle', 'mp3', 'beef', 'vase', 'lip', 'fake', 'shovel', 'remote', 'pencil', 'peanuts', 'picture', 'doll', 'cat', 'sponge', 'tote', 'drive', 'pants', 'packing', 'apple', 'hanger', 'bookmark', 'file', 'speakers', 'eraser', 'television', 'checkbook', 'phone', 'playing', 'clothes', 'pillow', 'chair', 'blouse', 'credit', 'clock', 'air', 'watch', 'clay', 'cinder', 'cork', 'press', 'bowl', 'flowers', 'containers', 'container', 'toe', 'drawer', 'coasters', 'blanket', 'spoon', 'CD', 'screw', 'house', 'plastic', 'truck', 'newspaper', 'wrapper', 'sandal', 'needle', 'album', 'tray', 'shoe', 'clippers', 'sand', 'thermometer', 'nail', 'socks', 'wallet', 'plate', 'sun', 'rubber', 'window', 'block', 'charger', 'car', 'desk', 'cup', 'tie', 'freshener', 'basket', 'tape', 'slipper', 'brocolli', 'sauce', 'chain', 'door', 'cups', 'cell', 'key', 'pots', 'shirt', 'ice', 'greeting', 'food', 'computer', 'toilet', 'soap', 'games', 'shade', 'pen', 'lights', 'USB', 'tissue', 'ipod', 'packet', 'tv', 'warmers', 'rusty', 'lamp', 'table', 'soy', 'wagon', 'player', 'carrots', 'bow', 'note', 'sidewalk', 'model', 'towel', 'water', 'twezzers', 'piano', 'lace', 'scotch', 'thread', 'keys', 'bottle', 'tire', 'knife', 'monitor', 'chocolate', 'belt', 'stop', 'keyboard', 'grid', 'fridge', 'cans', 'shawl', 'box', 'perfume', 'bananas', 'spring', 'sofa', 'swing', 'rugs', 'zipper', 'toothbrush', 'money', 'boom', 'ring', 'leg', 'washing', 'book', 'candle', 'cap', 'bracelet', 'face', 'tomato', 'lotion', 'shoes', 'purse', 'button', 'eye', 'picks', 'twister', 'cube', 'brush', 'mop', 'sticky', 'rug', 'chapter',
                     'can', 'jewlery', 'envelope', 'machine', 'totes', 'gloss', 'hair', 'tablet', 'radio', 'wash', 'candy', 'deodorant', 'stockings', 'headphones', 'drill', 'duck', 'floor', 'furniture', 'jar', 'thermostat', 'bag', 'sign', 'conditioner', 'glass', 'couch', 'bed', 'pad', 'controller', 'canvas', 'sailboat', 'cookie', 'outlet', 'mouse', 'paint', 'sharpie', 'frame', 'toothpaste', 'photo', 'mirror', 'pool', 'camera', 'paper', 'bread', 'chalk', 'card', 'tree', 'glasses', 'jugs'}
    
    data1 = dict()
    # check if <p> is in website
    if temp != "":
        # <p> text in site
        for paragraph in temp:
            # keywords like recycle, reuse, DIY
            for keyword in keywords:
                # checks to see if keyword is in paragraph
                if keyword in str(paragraph):
                    # gets common object from common objects set
                    for obj in commonObjects:
                        obj in str(paragraph)
                        # checks to see if common object is in the paragraph
                        if obj in str(paragraph):
                            if obj not in data1.keys():
                                data1[obj] = [[url, paragraph]]
                            else:
                                temp = data1[obj]
                                temp.append([url, paragraph])
                                data1[obj] = temp
    else:
        return False
    return data1

print(scraper(url))
stop = timeit.default_timer()
print('Time: ', stop - start)

# str1 = "book eraser model car boom box tomato rusty nail door sandal perfume helmet fridge speakers candle pillow wallet sailboat teddies cork twezzers food lace buckle bookmark ice cube tray chair eye liner soap bracelet rubber duck stockings box packing peanuts bottle cap rubber band shirt sofa greeting card paper ring face wash bag twister lamp television grid paper milk doll money playing card toilet mirror lamp shade clay pot sidewalk tv pants window shampoo thermostat puddle cell phone mop car tire swing soda can scotch tape mouse pad stop sign socks sun glasses glasses cup bowl clock vase bow chocolate mp3 player candy wrapper clamp headphones pool stick lip gloss hair brush bananas conditioner shoe lace clothes drill press shawl glow stick remote sand paper leg warmers tree CD piano brocolli washing machine fake flowers canvas fork bottle slipper pencil bed keyboard radio key chain thermometer cat video games toothpaste sticky note nail file hair tie seat belt flowers thread sharpie plastic fork air freshener keys soy sauce packet watch water bottle shovel house toe ring spoon cinder block paint brush street lights screw button table carrots bread spring desk drawer computer pen flag USB drive sketch pad charger magnet blouse white chair knife checkbook truck lotion wagon toothbrush tissue box photo album zipper tooth picks towel picture frame purse glass balloon blanket ipod chapter book floor plate hanger newspaper credit card chalk beef rug camera deodorant coasters outlet phone shoes apple sponge nail clippers cookie jar monitor controller needle couch twister ice cube tray chocolate bow coasters monitor rug beef camera keys twezzers headphones perfume soy sauce packet controller sand paper hair tie clamp street lights hair brush conditioner soap blanket chapter book cookie jar toothbrush shirt thermometer CD drill press shoes doll shampoo apple flowers pencil toothpaste bread flag bottle house sharpie hanger watch magnet rubber duck towel cork charger shawl boom box paper thread bookmark air freshener rubber band newspaper sticky note model car face wash USB drive pillow tire swing nail clippers eye liner chair car sponge key chain cell phone shoe lace toe ring clay pot book box nail file sofa cinder block television eraser mirror greeting card helmet carrots stockings screw washing machine white out bag wagon sandal playing card slipper door outlet speakers lip gloss bowl computer photo album toilet bananas chalk glass candy wrapper glasses paint brush mouse pad milk couch tissue box mp3 player bed candle wallet pen piano socks truck lamp shade needle balloon deodorant table leg warmers bottle cap lotion clothes tooth picks scotch tape button radio clock rusty nail cup water bottle packing peanuts teddies lace stop sign cat spring buckle canvas tree ring fake flowers shovel fridge knife tomato lamp pants desk thermostat sketch pad ipod plastic fork spoon fork seat belt remote window video games brocolli vase food glow stick floor credit card sailboat plate drawer soda can sidewalk blouse phone checkbook grid paper money bracelet zipper keyboard tv puddle purse mop picture frame pool stick sun glasses bow clay pot helmet paper television mp3 player USB drive wagon milk chair sticky note deodorant paint brush greeting card slipper eye liner stop sign headphones cinder block shawl house keys thermostat book bowl sponge toilet twister glow stick twezzers spring tire swing hair brush cell phone truck brocolli white out ring drill press toothpaste piano fridge playing card screw thread shoes clamp mirror mouse pad flag sailboat cup charger conditioner couch watch blanket key chain doll hanger clothes buckle needle toothbrush sidewalk boom box street lights car air freshener tooth picks computer zipper washing machine nail file window face wash bed camera shoe lace grid paper credit card flowers box towel glasses canvas soda can table scotch tape mop soap tree shampoo nail clippers pants ipod rug checkbook soy sauce packet tomato magnet chocolate apple fork puddle sharpie rubber duck pen lotion fake flowers cookie jar toe ring glass floor sofa thermometer balloon bottle tv spoon lamp shade eraser keyboard phone plastic fork sun glasses seat belt outlet bread CD pillow chapter book blouse lip gloss rubber band cat newspaper stockings hair tie knife clock video games door candle carrots bag money bottle cap chalk pencil model car water bottle sketch pad coasters perfume socks button teddies candy wrapper picture frame ice cube tray purse cork shovel tissue box food lamp plate rusty nail leg warmers monitor packing peanuts lace bracelet desk sand paper pool stick wallet speakers bookmark sandal radio vase remote photo album shirt drawer bananas controller beef beef hair tie couch twister cookie jar shovel desk lamp shade phone model car clock toe ring toothbrush chalk thread hanger spoon nail clippers candy wrapper water bottle toothpaste table socks boom box deodorant rusty nail teddies plastic fork spring bowl floor bananas face wash hair brush piano video games cork bed bag shampoo flag credit card money television drill press sun glasses window leg warmers truck flowers sticky note controller box conditioner bottle shawl sand paper rubber duck mop helmet toilet soap grid paper eraser headphones blouse ring sailboat sandal chapter book monitor button car fake flowers photo album sponge street lights ice cube tray white out brocolli shirt speakers zipper eye liner paint brush sidewalk slipper tree pants knife shoes glow stick rubber band sharpie drawer stockings blanket seat belt plate chocolate keyboard tomato wallet wagon purse lip gloss newspaper stop sign book lamp watch candle pen soy sauce packet food tv USB drive bottle cap coasters tire swing key chain remote computer sofa packing peanuts mp3 player outlet cinder block pool stick sketch pad ipod carrots glass clamp magnet house air freshener screw puddle vase rug paper canvas towel charger door lace fork radio nail file needle pencil twezzers tooth picks tissue box buckle lotion bracelet cell phone greeting card cat doll bookmark playing card milk balloon bread washing machine mirror fridge checkbook shoe lace camera mouse pad thermostat thermometer glasses soda can bow cup CD pillow chair apple clay pot clothes keys scotch tape perfume picture frame packing peanuts rubber duck spring ipod radio bag lip gloss mop perfume bow white out sofa headphones conditioner watch model car purse wallet car cinder block paint brush CD thermometer soy sauce packet chalk couch nail file zipper clamp screw shampoo greeting card glass soap tv glasses washing machine eye liner rusty nail apple table fake flowers fork paper coasters leg warmers chapter book seat belt bottle cap stop sign sketch pad clothes drill press cell phone toilet vase brocolli buckle bowl sailboat bread toothpaste tooth picks bracelet scotch tape photo album remote plate television face wash fridge hanger tree towel spoon plastic fork shoe lace doll playing card hair brush slipper carrots candle milk shawl USB drive water bottle pencil pen drawer knife key chain tissue box nail clippers grid paper cat twezzers socks computer phone flag boom box bookmark door keys lamp shade sand paper floor charger credit card video games twister deodorant air freshener truck bananas speakers thermostat clock rug lotion chocolate lamp window tomato keyboard cookie jar pants mp3 player soda can ring clay pot cup flowers sun glasses bed toothbrush glow stick pool stick candy wrapper rubber band magnet blouse mirror shoes monitor pillow chair sponge money puddle needle sidewalk helmet picture frame balloon sandal mouse pad street lights shirt food canvas shovel controller eraser sticky note stockings wagon desk lace book newspaper bottle house sharpie cork outlet piano camera box beef hair tie teddies checkbook tire swing toe ring button blanket ice cube tray thread money flowers shoes air freshener boom box spring spoon lace vase floor photo album hanger bed puddle blanket picture frame car paint brush shoe lace watch brocolli leg warmers hair brush twister sticky note pillow slipper USB drive tomato thermometer bracelet candy wrapper bananas rug thread box lip gloss eye liner sofa plate carrots fake flowers socks television food twezzers cinder block toilet bread cell phone lamp washing machine shirt pen wagon rubber duck purse playing card thermostat buckle tree outlet sidewalk desk packing peanuts computer cork keyboard tire swing candle apple fridge book deodorant perfume bottle cap cat sandal sponge camera water bottle headphones flag video games nail clippers sun glasses grid paper soap piano checkbook helmet knife mirror door monitor newspaper zipper truck hair tie tv shampoo plastic fork toe ring bow chair mp3 player soy sauce packet clothes conditioner coasters face wash sharpie lotion greeting card scotch tape tissue box seat belt mouse pad cup canvas couch toothbrush pencil magnet screw drill press shawl controller sand paper model car radio clock sketch pad wallet sailboat phone soda can table street lights drawer ice cube tray glow stick pants ring eraser clay pot pool stick chalk stockings key chain needle shovel charger bookmark stop sign button cookie jar chapter book lamp shade glass remote rubber band milk bottle rusty nail bag speakers beef white out blouse toothpaste paper window chocolate teddies keys fork towel mop nail file clamp bowl credit card balloon glasses doll CD house tooth picks ipod spring tree key chain bracelet cell phone towel water bottle face wash spoon clay pot food door thermostat sand paper soy sauce packet bottle cap car apple hanger coasters wallet flag cookie jar headphones lace bottle mp3 player blanket toilet toothpaste knife cork desk shoe lace chapter book screw newspaper sun glasses bookmark fridge bag sofa magnet remote canvas fork tv credit card picture frame lip gloss clock wagon cinder block air freshener boom box USB drive thread ring drill press clothes clamp tablet phone container containers monitor cups cans basket envelope clothes rugs dresses pots tote totes pots furniture jewlery bag"
# str1 = str1.split(" ")
# str1 = set(str1)
# print(str1)
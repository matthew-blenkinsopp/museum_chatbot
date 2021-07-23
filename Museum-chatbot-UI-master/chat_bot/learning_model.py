import os

import pandas as pd
from chat_bot.models import Question


class ChatModel():
    keyWords = [
        ['email', 'speak', 'contact', 'manager', 'contacts', 'contact det', 'who do i', 'who should i', 'right pers'
            , 'who to', 'who', 'real person', 'real person', 'real person'],
        ['image', 'photo', 'photo', 'image', 'image', 'get an image', 'track down a photo', 'copy of the portrait'],
        ['information', 'interest', 'know', 'enquir', 'information', 'learn', 'information', 'information', 'know more',
         'learn more'],
        ['eat', 'lunch'],
        ['how long', 'long'],
        ['press', 'press', 'discount'],
        ['free', 'military', 'service', 'airforce', 'cheap'],
        ['supervis', 'child', 'son', 'daughter', 'baby'],
        ['parent', 'pray', 'room', 'mosque', 'church'],
        ['oldest', 'oldest'],
        ['How many', 'been photo', 'have been photographed'],
        [],
        ['founding'],
        ['Museum sell'],
        [],
        ['animals'],
        ['treehouse', 'lolly'],
        ['audio-enabled', 'hear', 'impaired', 'deaf'],
        ['guns', 'swords', 'cool'],
        [],
        ['cite', 'object', 'reference'],
        ['taonga', 'back'],
        ['Collections', 'Online'],
        ['scientists', 'researchers', 'work', 'about the scientists', 'work at Auckland', 'resarcher at the musuem',
         'resarcher at the musuem'],
        ['correct', 'record', 'error', 'correct', 'wrong', 'mistake', 'update', 'change', 'update', 'update', 'wrong',
         'mistake', 'changed', 'be changed', 'mistake', 'incorrect', 'incorrect', 'incorrect', 'inaccurate', 'spelling',
         'spelling'],
        ['image', 'collection', 'order', 'order', 'copy for', 'get a print', 'get a print', 'article scanned',
         'scanned',
         'Do you have this image', 'buy a copy', 'license this image', 'license', 'license', 'permission to',
         'permission to', 'include this picture', 'include this picture', 'digital copy', 'digital copy',
         'include your photo', 'include your photo', 'scanned copy', 'following image', 'following image',
         'high resolution'],
        ['learn', 'find', 'out', 'more', 'information', 'find out more about', 'gaining more information'],
        ['CC-BY', 'copyright', 'copyright', 'copyright of', 'copyright of'],
        ['choose', 'collect', 'decide what is worth'],
        ['worth', 'much', 'value', 'worth', 'any value', 'any value', 'worth any', 'assess', 'its value', 'its value',
         'open market', 'open market', 'valued', 'valued'],
        [],
        [],
        [],
        ['kill', 'animal'],
        ['dead', 'bird', 'animal'],
        ['oldest', 'specimen', 'oldest specimen', 'oldest specimen'],
        ['why', 'specimens', 'important'],
        [],
        ['collection', 'human', 'history', 'human', 'human'],
        [],
        ['oldest book', 'oldest book', 'oldest book'],
        ['why', 'paper', 'important'],
        ['small', 'community', 'source', 'documents'],
        ['difference', 'library'],
        ['paper', 'collected', 'why', 'justified'],
        ['colonialism', 'library'],
        ['collection', 'library', 'view', 'library collections', 'library collections', 'read online', 'read online',
         'publication available online', 'publication available online'],
        ['difference', 'heritage', 'library'],
        ['join', 'library', 'borrow', 'books', 'borrowing object'],
        ['photocopy', 'library', 'photocopy'],
        ['flag', 'fly', 'half', 'why'],
        ['today', 'event', 'today', 'event'],
        ['wifi', 'wifi', 'wifi'],
        ['cafe', 'Columbus'],
        ['wheelchair', 'accessibl', 'for wheelchair', 'for wheelchair', 'Museum accessible', 'Museum accessible'],
        ['reserve', 'wheelchair', 'book', 'wheelchair'],
        ['tickets', 'assistants'],
        ['exhibition', 'put', 'put on an exhibition', 'on an exhibition', 'on an exhibition',
         'sponsoring an exhibition', 'sponsoring an exhibition?'],
        ['Shop', 'cafe', 'Library', 'Pou Maumahara', 'War Memorial space', 'free'],
        ['who own', 'owns the museum'],
        ['between the War Memorial Museum and the Auckland Museum',
         'between the War Memorial Museum and the Auckland Museum',
         'between the War Memorial Museum and the Auckland Museum'],
        ['difference', 'AWMM', 'auckland', 'war', 'AWMM', 'AWMM', 'difference'],
        ['change', 'name'],
        ['museums in Auckland', 'museums in Auckland', 'museums in Auckland', 'museums in Auckland', 'in Auckland',
         'other museum', 'other museum', 'only museum', 'only museum in Auckland', 'other museum', 'other museums',
         'other museums'],
        ['not on display', 'display', 'not on display', 'not on display?'],
        ['i touch', 'I touch', 'I touch'],
        ['dark', 'dim', 'no light', 'no light', 'dark', 'so dark', 'proper lighting', 'light', 'light'],
        ['shops', 'Centennial', '1866', 'Street'],
        ['Oceans', 'Coastal', 'galleries'],
        ['Armoury'],
        ['gold'],
        ['book', 'culture', 'performance'],
        [],
        ['curator', 'curator', 'curator', 'curator'],
        ['items I would like to donate', 'items I would like to donate', 'donat', 'item', 'donat', 'item', 'an item',
         'donat', 'donat', 'donat', 'would', 'interest', 'have', 'donate an item', 'donate an item', 'donate an item',
         'donating items', 'donate item', 'donate item', 'donation of', 'donation of', 'Would u like them',
         'Would u like them', 'accept the precious small amount of memorabilia', 'love to donate', 'happy to donate',
         'arrange delivery', 'donate them', 'add to its collection', 'add to its collection', 'Do you accept',
         'Do you accept', 'Would you like this', 'Would you like this', 'acquistion', 'acquistion', 'acquir', 'acquir',
         'acquir', 'any use to you', 'any use to you', 'be of use', 'to offer the'],
        ['hour', 'open', 'museum', 'close'],
        ['fee', 'entry', 'much is entry', 'cost', 'pay', 'pay', 'museum free', 'museum free', 'Museum cost',
         'cost of the museum', 'How much is the entry', 'pay to enter', 'Is the museum free', 'Is the museum free',
         'museum for free', 'Museum cost', 'entry fee', 'pay to enter', 'cost of the museum', 'pay to enter',
         'museum free',
         'museum for free'],
        ['public', 'transport', 'bus', 'get to the Museum', 'locat', 'locat', 'directions', 'directions'],
        ['park', 'cost', 'parking', 'parking'],
        ['prove', ' New Zealand', 'Aucklander', 'zealand', 'from auckland', 'from auckland'],
        ['anniversar', 'commemorate', 'celebrate', 'anzac', 'day'],
        ['lost', 'property', 'office', 'lost', 'item', 'lost'],
        ['why', 'eat', 'drink', 'galler', 'bring', 'food', 'food in the galleries', 'drink in the galleries',
         'drinks inside the museum', 'food inside the museum', 'food into the galleries', 'drinks into the galleries',
         'eat inside the museum', 'drinks into the galleries', 'food and beverage in collections',
         'policies concerning food'],
        ['bring', 'bring in', 'bag', 'with me', 'keep', 'inside', 'bring my bag', 'leave my bag', 'bring my bag',
         'keep my bag', 'keep my bag'],
        ['film', 'video', 'take photo', 'record', 'photos', 'inside', 'take a photo', 'take photo', 'while inside',
         'take photos inside',
         'photos of the exhibits', 'take videos inside', 'record inside', 'record inside', 'photos allowed',
         'videos while inside',
         'videos inside', 'videos inside', 'videos of the exhibits', 'videos of the exhibits',
         'photos of the collections',
         'take some photographs', 'take some photographs', 'take photos in the'],
        ['photo', 'maori', 'māori', 'portraits', 'māori', 'taonga', 'allow'],
        ['donat', 'money', 'donat', 'cash', 'donate to', 'monetary', 'donat', 'make donat', 'toward',
         'donate to the museum'
            , 'donate to the museum', 'money to the museum', 'money to the museum', 'donate to the museum'
            , 'donations to the museum', 'donations to the museum', 'donations to the museum', 'money to the museum'
            , 'donation to the museum', 'donate money', 'donate money', 'donate money', 'donate to the Museum'
            , 'donate money', 'donations to the museum', 'money to the museum', 'make a donation'],
        ['vacanc', 'job', 'hir', 'hir', 'intern', 'work for', 'job', 'job', 'vacanc', 'vacanc', 'opportun', 'opportun'
            , 'opportun', 'internship opportunities', 'jobs available', 'available jobs', 'jobs', 'jobs',
         'job vacancies'
            , 'internship', 'job', 'job', 'internships', 'looking for work', 'career', 'career', 'internship'
            , 'consider hiring someone', 'consider hiring someone', 'positions' 'positions', 'assistance',
         'assistance'],
        ['sell', 'art', 'shop'],
        ['ICOM', 'free', 'card'],
        ['roof', 'Event centre', 'Event centre', 'Event centre'],
        ['light', 'museum', 'cause', 'charity', 'company', 'event', 'birthday', 'anniversary'],
        ['consecrated', 'ground'],
        ['Wintergardens', 'open'],
        ['volunteer', 'volunteer', 'volunteer', 'volunteer', 'volunteer'],
        ['cenotaph', 'mean', 'cenotaph', 'explain'],
        ['Sir Edmund Hillary', 'Edmund Hillary', 'Edmund Hillary', 'Edmund Hillary', 'items of Sir Edmund Hillarys'
            , 'items related to Sir Edmund Hillary', 'items related to Sir Edmund Hillary'],
        ['founded', 'what year', 'creat', 'founded', 'creat', 'start'],
        ['history of the museum', 'history of the museum', 'history of the museum', 'history of the museum'
            , 'history of the museum'],
        ['open', 'Auckland', 'War', 'Memorial', 'when did the museum open', 'when did the museum open',
         'What year was the museum'
            , 'museum first open', 'museum first open', 'museum first open', 'official opening of the museum'
            , 'opening of the museum', 'museum officially opened'],
        ['Stained', 'glass', 'ceiling', 'Grand', 'Foyer'],
        ['Trust Board', 'execut', 'team', 'team', 'sits on the Trust Board', 'information about the trust board'
            , 'information about the executive team', 'members of the trust board', 'executive of the museum'
            , 'executive team of the museum', 'executive team of the museum', 'executive team members',
         'trust board members'
            , 'information regarding the trust board', 'information about the executive team', 'executive of the museum'
            , 'executive of the museum', 'executive team of the museum'],
        ['Taumata-ā-Iwi', 'Taumata-ā-Iwi', 'Taumata-ā-Iwi', 'maori trust', 'Māori trust', 'Māori trust'],
        ['Pacific', 'Advisory', 'Group', 'members'],
        ['join', 'Institute', 'apply', 'Institute', 'Institute', 'auckland museum institute',
         'auckland museum institute'],
        ['audio', 'guides', 'audio guide', 'audio guide'],
        ['research', 'specialt', 'what kind', 'type of'],
        ['speak', 'specialist', 'contact'],
        ['research', 'Museum', 'library', 'appointment', 'visit', 'visit the lib', 'visit', 'phd', 'phd'
            , 'research about my ancestors', 'research about my ancestors', 'Research library', 'Research library'
            , 'Research library', 'Research library', 'Research library', 'research visit', 'research visit'
            , 'research visit', 'doing some research', 'doing some research', 'visit your library', 'visit your library'
            , 'arrange to view', 'arrange to view', 'doing some research', 'private papers', 'private papers'
            , 'to view material', 'come into the library', 'visit the library'],
        ['Museum Studies', 'Museum Studies', 'Museum Studies', 'Museum Studies', 'information do you have on museums'],
        ['borrow an object', 'borrow an object', 'exhibition', 'borrow objects', 'borrow object', 'borrowing object'
            , 'borrowing object''loaning items', 'loaning items', 'loaning items', 'exhibition on loan'
            , 'exhibition on loan'],
        ['borrow books', 'borrow books', 'lend out books', 'lend out books', 'borrow a book', 'lend', 'book avail'
            , 'There is a book', 'There is a book', 'items at the library', 'items at the library', 'book available',
         'book available'],
        ['order', 'order', 'image', 'print of a photograph', 'prints of a photograph'
            , 'order images', 'request an image', 'image order', 'image order', 'order an image', 'order an image'
            , 'photocopy of this item', 'photocopy of this item', 'copy of the original photo', 'copy of the'
            , 'copy of the', 'copy of this photo', 'copy of this photo', 'copy of this', 'high resolution image'
            , 'high resolution image', 'order an image', 'prints of a photograph', 'order images', 'request an image'
            , 'image orders', 'order an image', 'photocopy of this item', 'copy of the original photo'],
        ['find', 'order', 'Museum', 'publications'],
        ['a book I wrote', 'a book I wrote', 'have new information', 'i wrote', 'want', 'i have', 'information'],
        ['military', 'personnel', 'file', 'access', 'file', 'family', 'personnel', 'records', 'father',
         'Military Personnel File', 'war record', 'dad', 'service record'],
        ['photographs of family', 'photographs', 'relative', 'war'],
        ['medal', 'relative', 'receive'],
        ['Cenotaph', 'relative', 'why', 'not', 'help', 'no record', 'isn\'t on'],
        ['Who', 'Online', 'Cenotaph', 'What record'],
        ['miss', 'Online', 'Cenotaph', 'record'],
        ['photograph', 'relative', 'Online', 'Cenotaph', 'add', 'add'],
        ['birth', 'death', 'not', 'appear'],
        ['identify', 'Medal', 'identify', 'identify'],
        ['service', 'record', 'service record', 'service record'],
        ['contribute', 'why', 'sections']
    ]

    def __init__(self):
        base = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        self.originalFAQs = pd.DataFrame(Question.objects.all().values("question", "answer"))
        self.cleanFAQQuestions = self.originalFAQs.iloc[:126, 0].values.tolist()
        self.cleanFAQAnswers = self.originalFAQs.iloc[:126, 1].values.tolist()

    def get_question(self, question):
        wordsCount = []
        for wordsIndex in range(len(self.keyWords)):
            words = self.keyWords[wordsIndex]
            count = 0
            if len(words) == 0:
                wordsCount.append(0)
                continue

            for word in words:
                if str(word).lower() in str(question).lower():
                    count += 1
            wordsCount.append(count)
        maxCount = max(wordsCount)
        maxIndexes = [ind for ind, j in enumerate(wordsCount) if j == maxCount]

        answer = Question.objects.filter(index=maxIndexes[0]+1).first()
        if answer.answer in ['nan', 'Nan', '', None]:
            return 'No answer available for now for question:' + answer.question + 'please contact <a href="https://www.aucklandmuseum.com/your-museum/contact-us">https://www.aucklandmuseum.com/your-museum/contact-us</a>'

        return answer.answer


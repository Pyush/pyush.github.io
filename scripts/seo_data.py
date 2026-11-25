"""Search and sharing data for every page, read by scripts/seo.py.

Keep each answer true to what the app page already says: these answers are shown on the
page and sent to search engines as structured data.
- title: about 50-62 characters, with the words people search for
- description: about 140-160 characters
- category: a schema.org applicationCategory that Google recognises
"""

SITE = 'https://ultimateplaystudio.com/'
BRAND = 'Ultimate Play Studio'
EMAIL = 'androidpyus@gmail.com'

HOME = {
    'title': 'Ultimate Play Studio – Private Apps & Games That Work Offline',
    'description': ('Ultimate Play Studio makes private apps and games: music, mental math, brain training, '
                    'puzzles, board and party games, voice notes, receipts and table scanning.'),
}

APPS = {
    'surjam': {
        'title': 'SurJam – Tabla, Sitar, Piano & Guitar App with Lessons',
        'description': ('Play 15 Indian and Western instruments on your phone: tabla, sitar, harmonium, bansuri, '
                        'piano, guitar and drums, with lessons, a tuner and a recorder.'),
        'category': 'MultimediaApplication', 'genre': 'Music',
        'share': 'Indian & Western instruments, lessons and a tuner',
        'faq': [
            ('Is SurJam free?',
             'Yes. SurJam is free to download and use. It shows ads from Google AdMob, and where the law requires it you are asked for consent first.'),
            ('Which instruments can I play in SurJam?',
             'Tabla, dholak and dhol, harmonium, sitar, bansuri, santoor, shehnai and veena, plus piano, guitar, ukulele, violin, xylophone, a 16-pad drum machine and a DJ loop launcher.'),
            ('Can I learn music with SurJam?',
             'Yes. There are step-by-step lessons for piano, guitar and tabla, ear training, a raga guide, a daily goal with practice streaks, and English or Sargam (Sa Re Ga) note labels.'),
            ('Does SurJam work offline, and do I need an account?',
             'SurJam works offline and needs no account or sign-up. Your recordings and progress stay on your phone, and the tuner analyses sound on your device without recording it.'),
        ],
    },
    'hokayantra': {
        'title': 'Hokayantra – Compass, Spirit Level, Ruler & Expense Tracker',
        'description': ('Offline toolkit: compass with True North, bubble level, ruler, metal detector, '
                        'flashlight, expense tracker, focus timer and HIIT workouts. 20 languages.'),
        'category': 'UtilitiesApplication', 'genre': 'Tools',
        'share': 'Compass, level, ruler, expenses, focus and workouts',
        'faq': [
            ('Is Hokayantra free?',
             'Yes. Hokayantra is free and shows ads from Google AdMob. Where the law requires it, you are asked for consent first.'),
            ('Does Hokayantra work offline?',
             'Yes. Every tool works without an internet connection, from the compass and spirit level to the expense tracker, focus timer and workout log.'),
            ('What tools are in Hokayantra?',
             'A compass with Magnetic and True North, GPS coordinates, bubble level, protractor, on-screen ruler, metal detector, magnifier, flashlight, unit converter, stopwatch, sound meter, the MoneyFlow expense tracker, the FocusFlow focus timer and workout timers.'),
            ('Which languages does Hokayantra support?',
             'English, Hindi, Bengali, Gujarati, Kannada, Malayalam, Marathi, Odia, Punjabi, Tamil, Telugu, Spanish, Portuguese, Indonesian, French, German, Japanese, Nepali, Assamese and Urdu.'),
        ],
    },
    'mathsurge': {
        'title': 'MathSurge – Mental Math Trainer, Vedic Maths & Brain Games',
        'description': ('Get faster at mental math with timed sprints, Vedic math tricks, Flash Anzan, MathDoku '
                        'and 2-player duels. 15 topics, practice for SAT, GRE, CAT and SSC.'),
        'category': 'EducationalApplication', 'genre': 'Education',
        'share': 'Mental math sprints, Vedic tricks and brain games',
        'faq': [
            ('Is MathSurge free?',
             'Yes. MathSurge is free and shows ads from Google AdMob. Where the law requires it, you are asked for consent first.'),
            ('Does MathSurge work offline?',
             'Yes. Every game works without an internet connection, and there is no sign-in or account. Your progress, streaks and history are stored only on your device.'),
            ('Can MathSurge help with exam preparation?',
             'Yes. You can practise for school maths and competitive exams such as SAT, GRE, GMAT, CAT, bank and SSC exams, with timed sprints across 15 topics and a Mistake Vault for spaced review.'),
            ('Does MathSurge teach Vedic math?',
             'Yes. The Tricks Academy covers mental math tricks and Vedic math sutras, and brain arenas such as Flash Anzan and Soroban build calculation speed.'),
        ],
    },
    'scribevault': {
        'title': 'ScribeVault – Private Voice to Text, Offline AI Transcription',
        'description': ('Record meetings, lectures and voice notes and transcribe them on your phone in 18 languages. '
                        'Speaker labels, summaries, action items. Encrypted, no ads.'),
        'category': 'BusinessApplication', 'genre': 'Productivity',
        'share': 'On-device transcription, speakers and summaries',
        'faq': [
            ('Are my recordings uploaded?',
             'No. Audio is transcribed on your device and never sent to a server. The internet is used only to download speech models and for Google Play billing.'),
            ('Does ScribeVault work offline?',
             'Yes. Speech-to-text runs on your phone, offline after a one-time model download.'),
            ('Which languages does ScribeVault transcribe?',
             'ScribeVault transcribes 18 languages, each in its own script, including Hindi in Devanagari, and it can translate speech into English.'),
            ('Is ScribeVault free?',
             'ScribeVault is free to download and includes 3 transcriptions a week, up to 2 minutes each. ScribeVault Pro, a monthly or yearly subscription through Google Play, removes the weekly limit and the 2-minute cap and adds PDF export.'),
        ],
    },
    'undercover': {
        'title': 'Undercover: Word Impostor – Party Game for 3 to 12 Players',
        'description': ('Pass-and-play word party game on one phone. Find the impostor with Civilian, Undercover and '
                        'Mr. White roles, 85 word pairs and custom words. Plays offline.'),
        'category': 'GameApplication', 'genre': 'Party game',
        'share': 'Find the impostor: a party game on one phone',
        'faq': [
            ('How do you play Undercover?',
             'Pass the phone so each player privately sees their word. Civilians share a word, the Undercover gets a similar one, and Mr. White gets no word and has to bluff. Give one-word clues, discuss and vote someone out.'),
            ('How many players does Undercover need?',
             'Undercover is for 3 to 12 players on a single device.'),
            ('Is Undercover free?',
             'Yes. Undercover is free to play with ads from Google AdMob. You can watch a short optional ad to unlock custom word packs, and there are no in-app purchases.'),
            ('Does Undercover work offline?',
             'Yes. Gameplay works offline and there is no sign-in or account. Player names, custom words and match stats stay on your phone.'),
        ],
    },
    'rasidly': {
        'title': 'Rasidly – Offline Receipt Scanner, GST Report & Bill Reminders',
        'description': ('Scan receipts on your phone with no internet and no account. GST input tax credit reports, '
                        'bill and warranty reminders, document expiry alerts and budgets.'),
        'category': 'FinanceApplication', 'genre': 'Finance',
        'share': 'Offline receipts, GST reports and reminders',
        'faq': [
            ('Are my receipts uploaded?',
             'No. Receipts are read and stored on your phone and never uploaded. The internet is used only for Google Play billing and for usage metrics that Google ML Kit sends about text recognition.'),
            ('Does Rasidly make GST reports?',
             'Yes. Rasidly records GST, VAT or sales tax on every receipt and makes a GST input tax credit report with CGST, SGST, IGST and cess, by tax year or quarter. Rasidly keeps records and does not give tax advice.'),
            ('Is Rasidly free?',
             'Rasidly is free to download and includes 10 scans a month, bills and reminders, insights, one budget, the GST report, one warranty and two documents. Rasidly Pro, a monthly or yearly subscription, adds unlimited scans, PDF and CSV exports and more.'),
            ('Does Rasidly have ads?',
             'No. There are no ads, no sign-in and no accounts.'),
        ],
    },
    'scanrow': {
        'title': 'Scanrow – Scan Tables & PDFs to Excel Spreadsheets (XLSX, CSV)',
        'description': ('Turn printed tables, price lists and PDF pages into editable spreadsheets with on-device '
                        'text recognition, then export to .xlsx or .csv. No account, no ads.'),
        'category': 'BusinessApplication', 'genre': 'Productivity',
        'share': 'Printed tables and PDFs to editable spreadsheets',
        'faq': [
            ('What file formats can Scanrow export?',
             'Scanrow exports a .xlsx spreadsheet or a .csv file, which you can send to a spreadsheet app, email or cloud drive.'),
            ('Can Scanrow read PDFs?',
             'Yes. Import a PDF or share one to Scanrow. It reads text directly from digital PDFs for exact results, and batch mode puts several pages in one workbook.'),
            ('Is Scanrow free?',
             'Scanrow is free to download. You can export or copy 3 scans every month and import PDFs of up to 20 pages at a time. Scanrow Pro, a monthly or yearly subscription, adds unlimited exports, larger PDFs and more recognition languages.'),
            ('Are my documents uploaded?',
             'No. Your documents are read and stored on your phone and leave it only when you export or share them. There are no ads and no accounts.'),
        ],
    },
    'kodijunction': {
        'title': 'Kodi Junction – Gujarati Cowrie Board Game like Chowka Bhara',
        'description': ('Play the classic Gujarati cowrie shell board game: race your gotis home against the computer, '
                        'pass and play on one phone, or play online with friends.'),
        'category': 'GameApplication', 'genre': 'Board game',
        'share': 'The classic cowrie board game from Gujarat',
        'faq': [
            ('How do you play Kodi Junction?',
             'Throw four cowrie shells and count the open ones to move 1 to 4, or 8 when all land closed. Capture rival gotis, stay safe on the X squares, and be first to bring all four gotis to the centre.'),
            ('Can I play Kodi Junction online with friends?',
             'Yes. Play online with 2, 3 or 4 players: invite friends with a link or match with anyone. You can also play the computer or pass and play on one phone.'),
            ('Does Kodi Junction work offline?',
             'Yes. Playing the computer and pass and play need no internet and no account.'),
            ('Is Kodi Junction free?',
             'Yes. Kodi Junction is free to play, with ads and optional in-app purchases. Ads never appear during a match, and the one-time Heritage Pro Pass removes banner and between-match ads.'),
        ],
    },
    'blokonia': {
        'title': 'Blokonia – Classic Falling Block Puzzle Game, Play Offline',
        'description': ('A classic falling block puzzle for phones: rotate and drop blocks, clear lines and chase '
                        'high scores in Classic, Daily Challenge, Sprint and Zen modes.'),
        'category': 'GameApplication', 'genre': 'Puzzle',
        'share': 'Classic falling blocks: Classic, Daily, Sprint and Zen',
        'faq': [
            ('What game modes does Blokonia have?',
             'Classic with endless levels that speed up, a Daily Challenge with the same pieces for everyone, Sprint to clear 40 lines as fast as you can, and Zen with no game over.'),
            ('Does Blokonia work offline?',
             'Yes. Blokonia works offline with no account to create, and your game saves automatically.'),
            ('Is Blokonia free?',
             'Yes. Blokonia is free to play, with ads and optional in-app purchases. Remove Ads, a one-time purchase, turns off banner and between-game ads.'),
            ('Is Blokonia accessible?',
             'Settings include colour-blind patterns and reduced motion, and sound, music and vibration can each be switched off.'),
        ],
    },
    'snakesladders': {
        'title': 'Snakes & Ladders: Editions – Classic Dice Board Game Offline',
        'description': ('The classic snakes and ladders dice game in five editions, including Moksha Patam. Play the '
                        'computer or pass and play with 2 to 4 players. Works offline.'),
        'category': 'GameApplication', 'genre': 'Board game',
        'share': 'The classic dice board game in five editions',
        'faq': [
            ('Which editions are included?',
             'Classic and High Contrast are free. Moksha Patam, Serpientes y Escaleras and Winding Path are one-time edition packs, and you can watch a short video to play a full demo game of any pack first.'),
            ('How many players can play?',
             'Play against one to three computer players, or pass and play with 2 to 4 players on one phone or tablet.'),
            ('Does Snakes & Ladders: Editions work offline?',
             'Yes. It works offline with no account to create.'),
            ('Is it accessible?',
             'Yes. It has full TalkBack support, so the board is described and every roll is read out, plus token shapes, arrows on snakes and ladders, reduced motion and large text.'),
        ],
    },
    'mergequest': {
        'title': 'Merge Quest: Discovery Puzzle – Relaxing Fantasy Merge Game',
        'description': ('Merge magical items, fill patron orders and restore a fading fantasy world. 64 items, weekly '
                        'events, no time limits on the main board and offline play.'),
        'category': 'GameApplication', 'genre': 'Puzzle',
        'share': 'A relaxing merge puzzle in a magical world',
        'faq': [
            ('How do you play Merge Quest?',
             'Drag two matching items together to make a higher-tier one, fill orders from the patrons who visit your board, and restore the world chapter by chapter.'),
            ('Does Merge Quest work offline?',
             'Yes. Merge Quest plays offline with no account to create.'),
            ('Is Merge Quest free?',
             'Yes. Merge Quest is free to play, with ads and optional in-app purchases. Remove Ads, a one-time purchase, turns off the banner and the in-between ads.'),
            ('Is there a time limit?',
             'No. There are no time limits on the main board, and undo, hints and auto-merge help when you are stuck.'),
        ],
    },
    'brainboost': {
        'title': 'BrainBoost – Brain Training Games for Memory, Focus & Math',
        'description': ('20 quick brain games for memory, focus, mental math and logic, a Daily Workout, a 75-second '
                        'Brain Age test and progress charts. Plays offline.'),
        'category': 'GameApplication', 'genre': 'Brain training',
        'share': '20 quick games for memory, focus, math and logic',
        'faq': [
            ('What games are in BrainBoost?',
             'Twenty games for memory, focus, math, logic and words, including Memory Matrix, Dual N-Back, Schulte Grid, Stroop Clash, Speed Math and Word Scramble, with a Daily Workout of three challenges picked for you.'),
            ('Does BrainBoost work offline?',
             'Yes. BrainBoost plays offline with no account to create. Signing in to Google Play Games is optional, for cloud save, leaderboards and achievements.'),
            ('Is the Brain Age test a medical test?',
             'No. BrainBoost is for fun and everyday mental practice. It is not a medical or diagnostic tool.'),
            ('Is BrainBoost free?',
             'Yes. BrainBoost is free to play, with ads that never appear during play. Remove Ads, a one-time purchase, turns off the banner and the in-between ads.'),
        ],
    },
}

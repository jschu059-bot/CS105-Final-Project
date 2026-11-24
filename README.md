# CS105-Final-Project

CS105 Fall 2026
Final Project
For your final project, you have three options to choose from:
1. Text Mining (described below)
2. Image Processing
3. Independent Project – You can choose a topic of your interest and work on a project of your choice.
If you choose either Option 2 or Option 3, you must meet with me, describe in detail what you would like to
work on, and obtain my approval before proceeding with the project.
Text Mining
This project focuses on building and analyzing a small text corpus for natural language processing and data
science tasks.
Start by joining a group of 4 – 6 students: https://docs.google.com/spreadsheets/d/1Lgld4JJUJkkj7mOIhOy-
F2T0hdfbeAKm/edit?usp=sharing&ouid=107008399603089217757&rtpof=true&sd=true

Phase 1: Creating a Corpus (Deadline for Phase 1: November 21) 5%
In Phase 1, each group will create a corpus of documents. Each document should contain 1–2 sentences,
approximately 15–30 words. (If a student does not submit their vocabulary by the deadline, a 5% penalty
will apply, in addition to losing the 5% allocated to this part of the project.)
The documents will be constructed using the following content categories:
1. News, Politics, and Current Events
2. Computer Science and Data Science
3. Literature, Music, and TV
4. Health and Physical Activity
5. Food, Home, and Pets
For each content category, a short vocabulary list is provided. Your group must create 80–120 documents in
total (20 per team member).
o Each document must contain at least 3 words related to its assigned category or categories.
o Each document must contain at least 1 word from the provided vocabulary list for each assigned
category. (Any additional relevant words introduced by your group should be recorded in the
extended vocabulary list.)
o Half of the documents should focus on exactly one category.
o The other half should combine two categories.
o Approximately one-third of the documents should be positive, one-third negative, and one-third
neutral in sentiment.
o Each positive and negative document must include at least one word that clearly indicates the
corresponding sentiment.
Example Document 1: A new data system helps restaurants recommend better meals to customers. Users
report positive feedback and improved dining. Category: 2 and 5. Sentiment: Positive
Example Document 2: Some cats and dogs show signs of stress after routine changes at home. Their owners
notice weaker behavior and reduced activity. Category: 4 and 5. Sentiment: Negative
Submission format
Submit your corpus by uploading one Google Sheet file per group to the folder "Project Corpus". Label your
file as "Team N". Google Sheet should contain two sheets: Corpus and Extended Vocabulary.
Use the following format in the “Corpus” sheet: doc_id, text, category_1, category_2, sentiment. In addition:
o Use "none" for category_2 when a document belongs to only one category.
o For categories, use the category IDs from the project description. For example, News, Politics, and
Current Events should be labeled as 1.
o For sentiment, use one of the following labels exactly: Positive, Negative, Neutral.
o Each row should correspond to one document.
Use the following format in the "Extended Vocabulary" sheet: word, category_id, sentiment
Examples:
podcast 3 None
optimistic None Positive


Phase 2: Supervised Learning 40%
In this phase, use the corpus created in Phase 1 for supervised learning tasks.
Requirements:
o Read and tokenize the documents.
o Vectorize the corpus using Bag-of-Words (BoW) or one-hot encoding (OHE).
o Apply TF-IDF to the BoW representation, and compare the results with the original BoW
representation for at least some tasks.
Come up with at least four supervised learning tasks that can be accomplished using the labels and
structure of your corpus. Clearly describe each task. For each task: implement the methods, run
experiments, and analyze the results.
Use:
o Logistic Regression,
o K-Nearest Neighbors (kNN),
o Two additional supervised methods of your choice, for example, Naive Bayes, Support Vector
Machines (SVM), Decision Trees, Random Forest (or repeat the two techniques above, but for
different tasks).
For distance-based methods, use cosine similarity where appropriate. For at least two techniques, compare
cosine similarity with binary feature presence representations. Include visualizations where appropriate.


Phase 3: Unsupervised Learning 40%
In this phase, use the same corpus for unsupervised learning tasks.
Requirements:
o Use the same preprocessing and vectorization pipeline as in Phase 2.
o Come up with questions or exploratory questions that can be investigated using unsupervised
techniques and clearly describe them.
o Apply:
k-means clustering
hierarchical clustering
DBSCAN (optional)
Implement the methods, run experiments, and analyze the results.
Some questions to explore:
o Do documents naturally cluster by category or sentiment?
o Are mixed-category documents grouped differently from single-category documents?
o Which categories are most similar to each other?
Discuss:
o Whether the resulting clusters match the expected structure of the corpus,
o Which vectorization method produced more meaningful clusters,
Include visualizations where appropriate (for example, dendrograms or 2D projections).


Phase 4: VADER and Sentence-BERT 15%
In this phase, use pretrained NLP tools, VADER and Sentence-BERT (SBERT), and compare their
performance with the methods from Phases 2 and 3.
o Apply VADER for sentiment analysis on your corpus.
o Use SBERT embeddings for similarity, classification, or clustering tasks.
o Compare the results with the approaches used in Phases 2 and 3.
Discuss:
o whether pretrained models performed better than the methods from Phases 2 and 3,
o which tasks benefited most from SBERT embeddings,
o strengths and limitations of pretrained models on small datasets.
Split the work in such a way that each team member performs at least one supervised method and
one unsupervised method. All members are collectively responsible for the final submission.
What to submit:
1. Jupyter notebook, which should include all parts of the project (Google Drive, your team folder).
2. PDF version of your Jupyter notebook (Gradescope/Final Project/Teams).
3. Video recording and PowerPoint presentation (Google Drive, your team folder).
4. Answers to project questions (Gradescope/Answering Project Questions).
Jupyter notebook Provide your code, a detailed description of all the work, and your analysis. Follow the
order outlined in Project Phases 2 - 4. Begin with the project description. Describe each member’s
contribution at the end.
Writing questions Write three questions about your project and include them in your presentation slides.
All students should be able to answer all questions after watching your presentation (even if they were not
previously familiar with the topic).
Recording and demo For this part, you need to record an 8 –10-minute presentation covering all aspects of
your project and present it during a demo session.
Answering questions (to be completed individually and uploaded to Gradescope). Watch 8 presentations
prepared by other groups and respond to at least two questions from each presentation. Upload your
answers to Gradescope.

Timeline:
(1) Forming groups, completing Phase 1 – November 21.
(2) Completing Phase 2, Phase 3 – November 25, and December 3, respectively.
(3) Finishing, Uploading videos, slides, report – December 7.
(4) Presenting your project (over zoom, all team members must be present) – December 8.
(5) Answering questions – December 9.

Vocabulary lists:
News, Politics, and Current Events:
news, media, report, article, headline, election, vote, candidate, campaign, government, policy, law, senate,
congress, president, mayor, speech, debate, protest, economy, inflation, crisis, war, peace, global,
international, local, journalist, interview, public, reform, budget, tax, immigration, approval, coverage, update,
issue, official, discussion

Computer Science and Data Science:
algorithm, model, data, database, software, hardware, network, python, program, code, bug, feature, training,
testing, accuracy, prediction, classification, clustering, regression, variable, function, input, output, memory,
processor, cloud, analysis, statistics, visualization, matrix, token, corpus, vector, system, machine, learning,
interface, automation, query, storage

Literature, Music, and TV:
novel, poem, author, character, story, chapter, theme, drama, comedy, fantasy, music, song, melody, rhythm,
concert, album, artist, singer, instrument, lyrics, television, series, episode, actor, actress, director, script,
audience, streaming, performance, genre, review, scene, plot, dialogue, soundtrack, studio, production,
broadcast, entertainment

Health and Physical Activity:
health, exercise, fitness, workout, running, walking, cycling, yoga, strength, training, muscle, recovery,
nutrition, diet, sleep, energy, stress, mental, physical, injury, doctor, medicine, therapy, symptom, wellness,
hydration, routine, balance, cardio, movement, flexibility, endurance, prevention, healthy, habit, clinic,
treatment, breathing, posture, activity

Pets, Home, and Food:
cat, dog, pet, animal, owner, leash, toy, bowl, litter, training, home, kitchen, bedroom, furniture, garden,
laundry, cleaning, family, apartment, routine, food, meal, recipe, snack, fruit, vegetable, bread, soup, dinner,
breakfast, lunch, cooking, flavor, restaurant, ingredients, pantry, table, dish, coffee, grocery

Examples of positive sentiment words:
good, great, excellent, positive, happy, enjoyable, successful, effective, strong, useful, improved, pleasant,
helpful, exciting, satisfying

Examples of negative sentiment words:
bad, poor, negative, weak, difficult, stressful, harmful, disappointing, frustrating, slow, problematic,
concerning, serious, worse, failure

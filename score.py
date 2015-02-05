class Score():

    # When called, load the scoreboard from 'scoreboard.txt'
    def __init__(self):
        self.bestScores = self.loadScoreboard()

    # function loadScoreboard
    # Load a scoreboard from the text file
    def loadScoreboard(self):

        # If 'scoreboard.txt' exist, load it.
        # Elsewhere, create a 'scoreboard.txt' and return
        try:
            scoreboard = open('scoreboard.txt', 'r')
        except:
            scoreboard = open('scoreboard.txt', 'w')
            scoreboard.close()
            return []

        scores = scoreboard.readlines()
        bestScores = []

        for score in scores:
            score = score.strip('\n')
            score = score.split(" ")
            score[0] = int(score[0])
            bestScores.append(score)

        scoreboard.close()

        return bestScores

    # function printScoreboard
    # Print high scores in 'Score Name' format, up to top 10
    def printScoreboard(self):
        for score in self.bestScores:
            print ('{} {}'.format(score[0], score[1]))

    # function updateScoreboard
    # Given new (possibly) high score, update the 'scoreboard.txt'
    def updateScoreboard(self, score):
        bestScores = self.bestScores
        bestScores.append(score)
        bestScores.sort(reverse=True)

        # Only top 10 (or less) survives..
        bestScores = bestScores[:10]

        scoreboard = open('scoreboard.txt', 'w')
        for score in bestScores:
            score[1].strip('\n')
            scoreLine = str(score[0]) + " " + score[1] + '\n'
            scoreboard.write(scoreLine)

        scoreboard.close()

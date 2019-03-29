class HighScores(object):
    """Represents a player's scores.
    
    Attributes
    ---------
    scores : list
        a list of scores (int).

    Methods
    -------
    scores()
        Returns a list of all the scores.

    latest()
        Returns the latest score.

    personal_best()
        Returns the highest score.

    personal_top_three()
        Returns the three highest scores.
    """

    def __init__(self, scores):
        """
        Parameters
        ----------
        scores : list
            a list of scores (int).
        """
        self.scores = scores

    def scores(self):
        """Returns all the scores

        Returns
        -------
        list
            All the scores.
        """
        return self.scores 

    def latest(self):
        """Returns lastest score.

        Returns
        -------
        int
            The last item of the list of scores.
        """
        return self.scores[-1]

    def personal_best(self):
        """Returns the best score.

        Returns
        -------
        int
            The max value from the list of scores.
        """
        return max(self.scores)

    def personal_top_three(self):
        """Returns the three highest scores.

        Sorts the list of scores in descending order and
        returns the first three items.

        Returns
        -------
        list
            The three highest scores.
        """
        return sorted(self.scores, reverse=True)[:3]

    
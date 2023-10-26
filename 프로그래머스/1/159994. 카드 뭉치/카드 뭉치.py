def solution(cards1, cards2, goal):

    def can_form_goal(current_goal, remaining_cards1, remaining_cards2):
        if current_goal == goal:
            return True
        if len(current_goal) < len(goal):
            if remaining_cards1:
                if can_form_goal(current_goal + [remaining_cards1[0]], remaining_cards1[1:], remaining_cards2):
                    return True
            if remaining_cards2:
                if can_form_goal(current_goal + [remaining_cards2[0]], remaining_cards1, remaining_cards2[1:]):
                    return True
        return False

    return "Yes" if can_form_goal([], cards1, cards2) else "No"
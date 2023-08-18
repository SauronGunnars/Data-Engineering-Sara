from print_joke import get_random_reaction


def test_get_random_reaction_type():
    reaction = get_random_reaction()
    assert isinstance(reaction, str) # Replace False with a check that makes sure the reaction is a string type


def test_get_random_reaction_repeats():
    # Write a test that checks that multiple calls to get_random_reaction()
    # doesn't give you the same reaction every time
    reaction_list = []
    
    for i in range(2):
        reaction = get_random_reaction()
        assert reaction not in reaction_list
        reaction_list.append(reaction)

    


# Come up with a test of your own and implement it here.
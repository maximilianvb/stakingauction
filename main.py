import math

dict_of_accounts = {}
dict_of_auctions = {}


class User:

    def __init__(self, username, money):
        self.username = username
        self.money = float(money)


class Auction:
    def __init__(self, creator, item_name, starting_bid):
        self.bid_purgatory = {}
        self.item_name = item_name
        self.starting_bid = starting_bid
        self.current_bid = starting_bid
        self.current_holder = creator
        self.owner = creator
        self.shares = {self.owner: 100}

    def share_calculation(self, user, amount):
        price_change = amount / self.starting_bid
        share_delegation_ratio = price_change * 0.015
        new_shares = 0
        for holder in self.shares:
            new_shares += self.shares[holder] * share_delegation_ratio
            shares_to_cut = self.shares[holder] * share_delegation_ratio
            self.shares[holder] = self.shares[holder] - shares_to_cut
        self.shares[user] = new_shares
        self.current_bid = amount
        self.current_holder = user



def create_user():
    username = input("Please enter username: ")
    money = input("Please enter amount of money you have: ")
    dict_of_accounts[username] = User(username, money)


def create_auction():
    username = input("Please enter username: ")
    item_name = input("Please enter item name: ")
    starting_bid = float(input("Please enter starting bid: "))
    dict_of_auctions[item_name] = Auction(username, item_name, starting_bid)


def bid(auction, user, amount):
    new_user = user
    new_amount = amount
    if amount > dict_of_auctions[auction].current_bid:

        if dict_of_accounts[user].money >= amount:

            if not bool(dict_of_auctions[auction].bid_purgatory):
                dict_of_auctions[auction].bid_purgatory[user] = amount

            else:
                whoever_dude_is = ""
                for dude in dict_of_auctions[auction].bid_purgatory:
                    whoever_dude_is = dude
                    amount = dict_of_auctions[auction].bid_purgatory[dude]
                    dict_of_auctions[auction].share_calculation(dude, amount)

                del dict_of_auctions[auction].bid_purgatory[whoever_dude_is]
                dict_of_auctions[auction].bid_purgatory[new_user] = new_amount

        else:
            print("You don't have enough money!")

    else:
        print("The bid is too low!")

def calculate_payouts():
    for auction in dict_of_auctions:
        print("Picasso " + auction)
        print("Start price: " + str(dict_of_auctions[auction].starting_bid))
        print("Final price: " + str(dict_of_auctions[auction].current_bid))
        print("Winner of the auction is: " + str(dict_of_auctions[auction].bid_purgatory))

        for holder in dict_of_auctions[auction].shares:

            percentage_ownership = dict_of_auctions[auction].shares[holder] / 100
            payout = dict_of_auctions[auction].current_bid * percentage_ownership
            print(holder + " Payout: " + str(payout))

dict_of_accounts["Max"] = User("Max", 200)
dict_of_accounts["Carpaco"] = User("Carpaco", 50000000)
dict_of_accounts["Alice"] = User("Alice", 3000)
dict_of_accounts["Brook"] = User("Max", 50000)
dict_of_accounts["Brochester"] = User("Brochester", 1000)
dict_of_accounts["Gargoyle"] = User("Gargoyle", 2000)
dict_of_accounts["Jerome"] = User("Jerome", 1000)
dict_of_auctions["Tavla"] = Auction("Bob", "Tavla", 100)
bid("Tavla", "Max", 105)
bid("Tavla", "Jerome", 107)
bid("Tavla", "Brochester", 120)
bid("Tavla", "Gargoyle", 130)
bid("Tavla", "Brook", 140)
bid("Tavla", "Alice", 150)
bid("Tavla", "Carpaco", 200)
calculate_payouts()

import math
import unittest


def statement(invoice, plays):
    total_amount = 0
    volume_credits = 0
    result = f'Statement for {invoice["customer"]}\n'

    def format_as_dollars(amount):
        return f"${amount:0,.2f}"

    for perf in invoice['performances']:
        play = plays[perf['playID']]
        if play['type'] == "tragedy":
            this_amount = 40000
            if perf['audience'] > 30:
                this_amount += 1000 * (perf['audience'] - 30)
        elif play['type'] == "comedy":
            this_amount = 30000
            if perf['audience'] > 20:
                this_amount += 10000 + 500 * (perf['audience'] - 20)

            this_amount += 300 * perf['audience']

        else:
            raise ValueError(f'unknown type: {play["type"]}')

        # add volume credits
        volume_credits += max(perf['audience'] - 30, 0)
        # add extra credit for every ten comedy attendees
        if "comedy" == play["type"]:
            volume_credits += math.floor(perf['audience'] / 5)
        # print line for this order
        result += f' {play["name"]}: {format_as_dollars(this_amount / 100)} ({perf["audience"]} seats)\n'
        total_amount += this_amount

    result += f'Amount owed is {format_as_dollars(total_amount / 100)}\n'
    result += f'You earned {volume_credits} credits\n'
    return result


class TestStatement(unittest.TestCase):
    def test_statement_tragedy_gt_30_people(self):
        invoice = {
            "customer": "BigCo",
            "performances": [
                {
                    "playID": "othello",
                    "audience": 55
                }
            ]
        }
        plays = {
            "othello": {"name": "Othello", "type": "tragedy"}
        }
        response = "Statement for BigCo\n" \
                   " Othello: $650.00 (55 seats)\n" \
                   "Amount owed is $650.00\n" \
                   "You earned 25 credits\n"
        self.assertEqual(statement(invoice, plays), response)

    def test_statement_comedy_gt_20_people(self):
        invoice = {
            "customer": "BigCo",
            "performances": [
                {
                    "playID": "as-like",
                    "audience": 45
                }
            ]
        }
        plays = {
            "as-like": {"name": "As You Like It", "type": "comedy"}
        }
        response = "Statement for BigCo\n" \
                   " As You Like It: $660.00 (45 seats)\n" \
                   "Amount owed is $660.00\n" \
                   "You earned 24 credits\n"
        self.assertEqual(statement(invoice, plays), response)

    def test_statement_tragedy_lt_30_people(self):
        invoice = {
            "customer": "BigCo",
            "performances": [
                {
                    "playID": "hamlet",
                    "audience": 13
                }
            ]
        }
        plays = {
            "hamlet": {"name": "Hamlet", "type": "tragedy"}
        }
        response = "Statement for BigCo\n" \
                   " Hamlet: $400.00 (13 seats)\n" \
                   "Amount owed is $400.00\n" \
                   "You earned 0 credits\n"
        self.assertEqual(statement(invoice, plays), response)


if __name__ == '__main__':
    unittest.main()

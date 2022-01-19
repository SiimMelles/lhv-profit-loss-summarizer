# LHV profit/loss summarizer (Dividends for now)

import csv
from decimal import Decimal
from prettytable import PrettyTable

filename = "Realized_profit_loss_report.csv"

gains_table = PrettyTable()
dividends_table = PrettyTable()


def parse_lines(file_lines):
    gains = {}
    dividends = {}
    i = 0
    while i < len(file_lines):
        row = file_lines[i]
        if len(row) == 1 and row[0][0].isdigit():
            if row[0] == '1. Security transactions':
                # Skip header and blank space for now
                i += 3
                while len(file_lines[i]) != 0:
                    subrow = file_lines[i]
                    if subrow[5] != "":
                        if not (subrow[5] in gains):
                            gains[subrow[5]] = Decimal(subrow[20])
                        else:
                            gains[subrow[5]] += Decimal(subrow[20])
                    i += 1

            elif row[0] == '2. Dividend income':
                # Skip header and blank space for now
                i += 3
                while len(file_lines[i]) != 0:
                    subrow = file_lines[i]
                    if subrow[1] != "":
                        if not (subrow[1] in dividends):
                            dividends[subrow[1]] = Decimal(subrow[8])
                        else:
                            dividends[subrow[1]] += Decimal(subrow[8])
                    i += 1
        i += 1
    print("--- Profit/Loss from trades --")
    gains_table.add_column("Security", list(gains.keys()))
    gains_table.add_column("Profit/Loss", list(gains.values()))
    gains_table.align = "r"
    print(gains_table)
    print("\n")
    print("--- Gains from dividends ---")
    dividends_table.add_column("Security", list(dividends.keys()))
    dividends_table.add_column("Profit", list(dividends.values()))
    dividends_table.align = "r"
    print(dividends_table)


def read_file(name_of_file):
    read_lines = []
    with open(name_of_file, 'r', encoding='utf-8-sig') as csvfile:
        csvreader = csv.reader(csvfile)
        for line in csvreader:
            read_lines.append(line)

    return read_lines


if __name__ == '__main__':
    lines = read_file(filename)
    parse_lines(lines)

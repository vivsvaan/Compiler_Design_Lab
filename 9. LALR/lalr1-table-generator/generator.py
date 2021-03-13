from parsing import *
import grammar
import pandas as pd

def get_grammar():
    return grammar.get_sample_1()


def describe_grammar(gr):
    return '\n'.join([
        'Indexed grammar rules (%d in total):' % len(gr.productions),
        str(gr) + '\n',
        'Grammar non-terminals (%d in total):' % len(gr.nonterms),
        '\n'.join('\t' + str(s) for s in gr.nonterms) + '\n',
        'Grammar terminals (%d in total):' % len(gr.terminals),
        '\n'.join('\t' + str(s) for s in gr.terminals)
    ])


def describe_parsing_table(table):
    conflict_status = table.get_conflict_status()
    print("conflict status: ", conflict_status)
    def conflict_status_str(state_id):
        has_sr_conflict = (conflict_status[state_id] == lalr_one.STATUS_SR_CONFLICT)
        status_str = ('shift-reduce' if has_sr_conflict else 'reduce-reduce')
        return 'State %d has a %s conflict' % (state_id, status_str)

    return ''.join([
        'PARSING TABLE SUMMARY\n',
        'Is the given grammar LALR(1)? %s\n' % ('Yes' if table.is_lalr_one() else 'No'),
        ''.join(conflict_status_str(sid) + '\n' for sid in range(table.n_states)
                if conflict_status[sid] != lalr_one.STATUS_OK) + '\n',
        table.stringify()
    ])


def main():
    print('Reading Grammar Production Rules...')
    gr = get_grammar()
    print(describe_grammar(gr))
    print('Making Parsing Table...')
    table = lalr_one.ParsingTable(gr)
    print("Done\n")
    output_filename = 'parsing-table'

    with open(output_filename + '.txt', 'w') as textfile:
        textfile.write(describe_grammar(gr))
        textfile.write('\n\n')
        textfile.write(describe_parsing_table(table))

    table.save_to_csv(output_filename + '.csv')

    print("Parsing table is \n")
    parsing_table = pd.read_csv(output_filename + '.csv')
    header = []
    for i in parsing_table:
        header.append(i)

    parse_table = parsing_table.iloc[:,:].values
    for i in range(len(parse_table)):
        for j in range(len(header)):
            if str(parse_table[i][j]) == "nan":
                parse_table[i][j] = "  "
    print('{:^5}|'.format("state") + '{:^59}|'.format("action") + '{:^23}|'.format("goto"))
    for i in header:
        print('{:^5}|'.format(i),end="")
    print()
    for i in range(len(parse_table)):
        for j in range(len(header)):
            print('{:^5}|'.format(parse_table[i][j]), end="")
        print()
if __name__ == "__main__":
    main()

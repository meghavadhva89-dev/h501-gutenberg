from tt_gutenberg.authors import list_authors

if __name__ == '__main__':
    aliases = list_authors(alias=True, csv_path='data/gutenberg_authors.csv', alias_col='alias')
    print('Returned', len(aliases), 'aliases. Sample:', aliases[:20])

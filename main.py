from lib.Generator import Generator

G = Generator()

G.parse_permutations()

nfts_by_rarity = G.get_nfts_by_rarity()

for nft in G.nfts:
    nft.populate_imgs()
    nft.generate_image()


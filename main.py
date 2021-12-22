from lib.Generator import Generator

G = Generator()

# G.run()
G.parse_permutations()
print(G.nfts[0].layout)
# for nft in G.nfts:
#     nft.populate_imgs()
#     nft.generate_image()


from utils.chunker import chunkFiles

def main():
    chunks = chunkFiles()
    print(chunks)

if __name__ == "__main__":
    main()
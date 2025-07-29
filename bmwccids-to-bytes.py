def encode_ccid(ccid: int) -> tuple[int, int]:
    return ccid & 0xFF, ccid >> 8

def format_output(ccid: int, low: int, high: int) -> None:
    print(f"\nCCID {ccid} is in Hex: 0x{ccid:04X}")
    print(f"1st and 2nd byte: {{ 0x{low:02X}, 0x{high:02X} }}\n")

def main():
    while True:
        user_input = input("Enter CCID (or 'q' to quit): ").strip().lower()
        if user_input in ('q', 'quit', 'exit'):
            print("exiting...")
            break
        try:
            ccid = int(user_input)
            low, high = encode_ccid(ccid)
            format_output(ccid, low, high)
        except ValueError as e:
            print(f"Error: {e}\n")

if __name__ == "__main__":
    main()

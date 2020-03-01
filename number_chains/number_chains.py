
def number_chains(chain_number):
    """
    :param chain_number: int
    :return: string
    """
    output_log = []
    chained_numbers = [chain_number]
    
    for cn in chained_numbers:
        asc_chain_num = int("".join(sorted(str(cn))))
        desc_chain_num = int("".join(sorted(str(cn), reverse=True)))
        result = desc_chain_num - asc_chain_num
        output_log.append(f"{desc_chain_num} - {asc_chain_num} = {result}\n")
        chained_numbers.append(result)
        if result in chained_numbers[:-1]:
            return f"Original number was {chain_number}\n" \
                   f"{''.join(output_log)}" \
                   f"Chain length {len(chained_numbers) - 1}"


print(number_chains(1234))

def remove_duplicates(tickets):
    unique_tickets = []
    for ticket_list in tickets.values():
        for ticket in ticket_list:
            if ticket not in unique_tickets:
                unique_tickets.append(ticket)
    return unique_tickets

def associate_criticality_with_tickets(types, tickets):
    unique_tickets = remove_duplicates(tickets)
    result = {}
    for criticality, ticket_list in tickets.items():
        current_criticality = types[criticality]
        result[current_criticality] = []
        for ticket in ticket_list:
            if ticket in unique_tickets:
                result[current_criticality].append(ticket)
                unique_tickets.remove(ticket)  
    return result
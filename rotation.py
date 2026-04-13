DOMAINS = ["domain1.com", "domain2.com", "domain3.com"]

def get_next_domain(index):
    return DOMAINS[index % len(DOMAINS)]
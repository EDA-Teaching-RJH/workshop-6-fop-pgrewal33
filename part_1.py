def sample_bay():
        samples = ["basalt", "silica", "iron", "dust"]
        print(samples[0])
        print(samples[1])
        print(samples[2])
        print(samples[-1])
        print (len(samples))
        return samples
        


def sample_analysis(samples):
        for i in range(len(samples)):
            print (f"transmitting data for: ", samples[i] )
sample_analysis(sample_bay())

def new_findings():
       new_findings = []
       for i in range(3):
            rock = input("type in a rock: ")
            new_findings.append(rock)
       print (new_findings)
new_findings()
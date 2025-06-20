import matplotlib.pyplot as plt

def radar_chart(skills, experience, keywords):
    labels = ['Skills', 'Experience', 'Keywords']
    values = [skills, experience, keywords]
    values += values[:1]
    angles = [n / float(len(labels)) * 2 * 3.14159 for n in range(len(labels))]
    angles += angles[:1]

    fig, ax = plt.subplots(figsize=(5, 5), subplot_kw=dict(polar=True))
    ax.plot(angles, values, 'o-', linewidth=2)
    ax.fill(angles, values, alpha=0.25)
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(labels)
    ax.set_title("Resume vs Job Match")
    return fig

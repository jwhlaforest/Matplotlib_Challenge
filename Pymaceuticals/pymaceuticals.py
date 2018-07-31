
# Dependencies and Setup
%matplotlib inline
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Hide warning messages in notebook
import warnings
warnings.filterwarnings('ignore')

# File to Load (Remember to Change These)
mouse_drug_data_to_load = "data/mouse_drug_data.csv"
clinical_trial_data_to_load = "data/clinicaltrial_data.csv"

# Read the Mouse and Drug Data and the Clinical Trial Data
m_d_data = pd.read_csv(mouse_drug_data_to_load)
c_t_data = pd.read_csv(clinical_trial_data_to_load)
print(m_d_data.head())
print(c_t_data.head())

# Combine the data into a single dataset
combined_data = pd.merge(m_d_data, c_t_data, how='left', on='Mouse ID')

# Display the data table for preview
combined_data.head()

## Tumor Response to Treatment

# Store the Mean Tumor Volume Data Grouped by Drug and Timepoint 
t_v_mean = combined_data.groupby(['Drug', 'Timepoint']).mean()['Tumor Volume (mm3)']

# Convert to DataFrame
t_v_mean = pd.DataFrame(t_v_mean)

# Preview DataFrame
t_v_mean.head(20)

# Store the Standard Error of Tumor Volumes Grouped by Drug and Timepoint
t_v_se = combined_data.groupby(['Drug', 'Timepoint']).sem()['Tumor Volume (mm3)']

# Convert to DataFrame
t_v_se = pd.DataFrame(t_v_se)

# Preview DataFrame
t_v_se.head(20)

# Minor Data Munging to Re-Format the Data Frames
t_v_mean = t_v_mean.reset_index()
t_v_piv_mean = t_v_mean.pivot(index='Timepoint', columns='Drug')['Tumor Volume (mm3)']

t_v_se = t_v_se.reset_index()
t_v_piv_se = t_v_se.pivot(index='Timepoint', columns='Drug')['Tumor Volume (mm3)']

# Preview that Reformatting worked
# t_v_piv_mean
t_v_piv_se

# Generate the Plot (with Error Bars)
plt.errorbar(t_v_piv_mean.index, t_v_piv_mean['Placebo'], yerr=t_v_piv_se['Placebo'], color='black', marker='o', linestyle='-' , linewidth=0.7, markersize=3)
plt.errorbar(t_v_piv_mean.index, t_v_piv_mean['Capomulin'], yerr=t_v_piv_se['Capomulin'], color='red', marker='v', linestyle='--' , linewidth=0.5, markersize=3)
plt.errorbar(t_v_piv_mean.index, t_v_piv_mean['Ceftamin'], yerr=t_v_piv_se['Ceftamin'], color='orange', marker='^', linestyle='--' , linewidth=0.5, markersize=3)
plt.errorbar(t_v_piv_mean.index, t_v_piv_mean['Infubinol'], yerr=t_v_piv_se['Infubinol'], color='yellow', marker='<', linestyle='--' , linewidth=0.5, markersize=3)
plt.errorbar(t_v_piv_mean.index, t_v_piv_mean['Ketapril'], yerr=t_v_piv_se['Ketapril'], color='green', marker='>', linestyle='--' , linewidth=0.5, markersize=3)
plt.errorbar(t_v_piv_mean.index, t_v_piv_mean['Naftisol'], yerr=t_v_piv_se['Naftisol'], color='blue', marker='8', linestyle='--' , linewidth=0.5, markersize=3)
plt.errorbar(t_v_piv_mean.index, t_v_piv_mean['Propriva'], yerr=t_v_piv_se['Propriva'], color='purple', marker='s', linestyle='--' , linewidth=0.5, markersize=3)
plt.errorbar(t_v_piv_mean.index, t_v_piv_mean['Ramicane'], yerr=t_v_piv_se['Ramicane'], color='salmon', marker='p', linestyle='--' , linewidth=0.5, markersize=3)
plt.errorbar(t_v_piv_mean.index, t_v_piv_mean['Stelasyn'], yerr=t_v_piv_se['Stelasyn'], color='coral', marker='P', linestyle='--' , linewidth=0.5, markersize=3)
plt.errorbar(t_v_piv_mean.index, t_v_piv_mean['Zoniferol'], yerr=t_v_piv_se['Zoniferol'], color='darkkhaki', marker='*', linestyle='--' , linewidth=0.5, markersize=3)

plt.gcf().set_facecolor('white')
plt.title('Tumor Volume Change')
plt.ylabel('Tumor Volume (mm3)')
plt.xlabel('Time (Days)')
lgd = plt.legend(loc=7, bbox_to_anchor=(1.25, 0.5), fontsize='small')
plt.grid(True)

# Save the Figure
plt.savefig('analysis/TumorVolumeChange', bbox_extra_artists=(lgd,), bbox_inches='tight', dpi=150)

# Show the Figure
plt.show()

## Metastatic Response to Treatment

# Store the Mean Met. Site Data Grouped by Drug and Timepoint 
met_mean = combined_data.groupby(['Drug', 'Timepoint']).mean()['Metastatic Sites']

# Convert to DataFrame
met_mean = pd.DataFrame(met_mean)

# Preview DataFrame
met_mean.head(20)

# Store the Standard Error associated with Met. Sites Grouped by Drug and Timepoint 
met_se = combined_data.groupby(['Drug', 'Timepoint']).sem()['Metastatic Sites']

# Convert to DataFrame
met_se = pd.DataFrame(met_se)

# Preview DataFrame
met_se.head(20)

# Minor Data Munging to Re-Format the Data Frames
met_mean = met_mean.reset_index()
met_piv_mean = met_mean.pivot(index='Timepoint', columns='Drug')['Metastatic Sites']

met_se = met_se.reset_index()
met_piv_se = met_se.pivot(index='Timepoint', columns='Drug')['Metastatic Sites']

# Preview that Reformatting worked
# met_piv_mean
met_piv_se

# Generate the Plot (with Error Bars)
plt.errorbar(met_piv_mean.index, met_piv_mean['Placebo'], yerr=met_piv_se['Placebo'], color='black', marker='o', linestyle='-' , linewidth=0.7, markersize=3)
plt.errorbar(met_piv_mean.index, met_piv_mean['Capomulin'], yerr=met_piv_se['Capomulin'], color='red', marker='v', linestyle='--' , linewidth=0.5, markersize=3)
plt.errorbar(met_piv_mean.index, met_piv_mean['Ceftamin'], yerr=met_piv_se['Ceftamin'], color='orange', marker='^', linestyle='--' , linewidth=0.5, markersize=3)
plt.errorbar(met_piv_mean.index, met_piv_mean['Infubinol'], yerr=met_piv_se['Infubinol'], color='yellow', marker='<', linestyle='--' , linewidth=0.5, markersize=3)
plt.errorbar(met_piv_mean.index, met_piv_mean['Ketapril'], yerr=met_piv_se['Ketapril'], color='green', marker='>', linestyle='--' , linewidth=0.5, markersize=3)
plt.errorbar(met_piv_mean.index, met_piv_mean['Naftisol'], yerr=met_piv_se['Naftisol'], color='blue', marker='8', linestyle='--' , linewidth=0.5, markersize=3)
plt.errorbar(met_piv_mean.index, met_piv_mean['Propriva'], yerr=met_piv_se['Propriva'], color='purple', marker='s', linestyle='--' , linewidth=0.5, markersize=3)
plt.errorbar(met_piv_mean.index, met_piv_mean['Ramicane'], yerr=met_piv_se['Ramicane'], color='salmon', marker='p', linestyle='--' , linewidth=0.5, markersize=3)
plt.errorbar(met_piv_mean.index, met_piv_mean['Stelasyn'], yerr=met_piv_se['Stelasyn'], color='coral', marker='P', linestyle='--' , linewidth=0.5, markersize=3)
plt.errorbar(met_piv_mean.index, met_piv_mean['Zoniferol'], yerr=met_piv_se['Zoniferol'], color='darkkhaki', marker='*', linestyle='--' , linewidth=0.5, markersize=3)

plt.gcf().set_facecolor('white')
plt.title('Metastatic Site Change')
plt.ylabel('Metastatic Sites')
plt.xlabel('Time (Days)')
lgd = plt.legend(loc=7, bbox_to_anchor=(1.25, 0.5), fontsize='small')
plt.grid(True)

# Save the Figure
plt.savefig('analysis/MetastaticSiteChange.png', bbox_extra_artists=(lgd,), bbox_inches='tight', dpi=150)

# Show the Figure
plt.show()

## Survival Rates

# Store the Count of Mice Grouped by Drug and Timepoint (W can pass any metric)
s_cnt = combined_data.groupby(['Drug', 'Timepoint']).count()['Tumor Volume (mm3)']

# Convert to DataFrame
s_cnt = pd.DataFrame({'Count': s_cnt})

# Preview DataFrame
s_cnt.head(20)

# Minor Data Munging to Re-Format the Data Frames
s_cnt = s_cnt.reset_index()
s_piv_cnt = s_cnt.pivot(index='Timepoint', columns='Drug')['Count']

# Preview the Data Frame
s_piv_cnt

# Generate the Plot (Accounting for percentages)
plt.plot(100 * s_piv_cnt['Placebo'] / 25, color='black', marker='o', linestyle='-', linewidth=0.7, markersize=3)
plt.plot(100 * s_piv_cnt['Capomulin'] / 25, color='red', marker='v', linestyle='--', linewidth=0.5, markersize=3)
plt.plot(100 * s_piv_cnt['Ceftamin'] / 25, color='orange', marker='^', linestyle='--', linewidth=0.5, markersize=3)
plt.plot(100 * s_piv_cnt['Infubinol'] / 25, color='yellow', marker='<', linestyle='--', linewidth=0.5, markersize=3)
plt.plot(100 * s_piv_cnt['Ketapril'] / 25, color='green', marker='>', linestyle='--', linewidth=0.5, markersize=3)
plt.plot(100 * s_piv_cnt['Naftisol'] / 25, color='blue', marker='8', linestyle='--', linewidth=0.5, markersize=3)
plt.plot(100 * s_piv_cnt['Propriva'] / 26, color='purple', marker='s', linestyle='--', linewidth=0.5, markersize=3)
plt.plot(100 * s_piv_cnt['Ramicane'] / 25, color='salmon', marker='p', linestyle='--', linewidth=0.5, markersize=3)
plt.plot(100 * s_piv_cnt['Stelasyn'] / 26, color='coral', marker='P', linestyle='--', linewidth=0.5, markersize=3)
plt.plot(100 * s_piv_cnt['Zoniferol'] / 25, color='darkkhaki', marker='*', linestyle='--', linewidth=0.5, markersize=3)

plt.gcf().set_facecolor('white')
plt.title("Mouse Survival")
plt.ylabel("Survival Rate (%)")
plt.xlabel("Time (Days)")
lgd = plt.legend(loc=7, bbox_to_anchor=(1.25, 0.5), fontsize='small')
plt.grid(True)

# Save the Figure
plt.savefig('analysis/SurvivalRate.png', bbox_extra_artists=(lgd,), bbox_inches='tight', dpi=150)

# Show the Figure
plt.show()

## Summary Bar Graph

# Calculate the percent changes for each drug
t_pct_chg_mean = 100 * (t_v_piv_mean.iloc[-1] - t_v_piv_mean.iloc[0]) / t_v_piv_mean.iloc[0]
t_pct_chg_se = 100 * (t_v_piv_se.iloc[-1] - t_v_piv_se.iloc[0]) / t_v_piv_se.iloc[0]

# t_pct_chg_mean = pd.DataFrame(t_pct_chg_mean)
# t_pct_chg_se = pd.DataFrame(t_pct_chg_se)

# Display the data to confirm
t_pct_chg_mean
# t_pct_chg_se

# Store all Relevant Percent Changes into a Tuple
pct_chg = (t_pct_chg_mean['Placebo'],
           t_pct_chg_mean['Capomulin'],
           t_pct_chg_mean['Ceftamin'],
           t_pct_chg_mean['Infubinol'],
           t_pct_chg_mean['Ketapril'],
           t_pct_chg_mean['Naftisol'],
           t_pct_chg_mean['Propriva'],
           t_pct_chg_mean['Ramicane'],
           t_pct_chg_mean['Stelasyn'],
           t_pct_chg_mean['Zoniferol'])

# Splice the data between passing and failing drugs
fig, ax = plt.subplots()
ticks = np.arange(len(pct_chg))
drg_fail_one = ax.bar(ticks[0], pct_chg[0], 1, color='red')
drg_pass_one = ax.bar(ticks[1], pct_chg[1], 1, color='green')
drg_fail_two = ax.bar(ticks[2:], pct_chg[2:], 1, color='red')
drg_pass_two = ax.bar(ticks[7], pct_chg[7], 1, color='green')
drg_fail_three = ax.bar(ticks[8:], pct_chg[8:], 1, color='red')

# Orient widths. Add labels, tick marks, etc. 
plt.gcf().set_facecolor('white')
ax.set_title('Tumor Volume Change')
ax.set_ylabel('% Tumor Volume Change')
ax.set_xticks(ticks)
plt.xticks(rotation='vertical')
ax.set_xticklabels(('Placebo',
                    'Capomulin',
                    'Ceftamin',
                    'Infubinol',
                    'Ketapril',
                    'Naftisol',
                    'Propriva',
                    'Ramicane',
                    'Stelasyn',
                    'Zoniferol'))
ax.grid()

# Use functions to label the percentages of changes
def pass_label(rects):
    for rect in rects:
        ht = rect.get_height()
        ax.text(rect.get_x() + rect.get_width() / 2, -8,
                '%d%%' % int(ht),
                ha='center', va='bottom', color='white')

def fail_label(rects):
    for rect in rects:
        ht = rect.get_height()
        ax.text(rect.get_x() + rect.get_width() / 2, 3,
                '%d%%' % int(ht),
                ha='center', va='bottom', color='white')

# Call functions to implement the function calls
pass_label(drg_pass_one)
fail_label(drg_fail_one)
pass_label(drg_pass_two)
fail_label(drg_fail_two)
fail_label(drg_fail_three)

# Save the Figure
fig.savefig('analysis/PercTumorVolumeChange.png', bbox_extra_artists=(lgd,), bbox_inches='tight', dpi=150)

# Show the Figure
fig.show()

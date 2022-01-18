###########################################################################################
#     Programming Project #3
#
#     Algorithm
#       loop while user requests
#           input data
#           loop while data incorrect
#           set irrelevant inputs to "no"/None
#           Advance to user preferences through if statements
#                calculate tuition
#           output formatted tuition
#
############################################################################################

############################################################################################
#################### Initialization of costs, taxes and loop conditions ####################
############################################################################################

# r = Resident
# nri = Non-Resident & International
# pc = Per Credit
# fr = Flat Rate
# be = Eli Broad College of Business & College of Engineering
# sf = Special Fees
# b = Business
# e = Engineering
# h = Health
# s = Sciences
# csme = CSME
# i = International
# js = Juniors and Seniors
# pt = Part Time
# ft = Full Time
# a = admitted
# jmc = James Madison College

restart = "yes"
not_valid_level = True
not_valid_credits = True
in_james_madison = "no"

freshman_r_pc = 482
freshman_r_fr = 7230
freshman_nri_pc = 1325.50
freshman_nri_fr = 19883

sophomore_r_pc = 494
sophomore_r_fr = 7410
sophomore_nri_pc = 1325.50
sophomore_nri_fr = 19883

junior_r_pc = 555
junior_r_fr = 8325
junior_nri_pc =1366.75
junior_nri_fr = 20501

senior_r_pc = 555
senior_r_fr = 8325
senior_nri_pc = 1366.75
senior_nri_fr = 20501

freshman_r_be_pc = 482
freshman_r_be_fr = 7230
freshman_nri_be_pc = 1325.50
freshman_nri_be_fr = 19883

sophomore_r_be_pc = 494
sophomore_r_be_fr = 7410
sophomore_nri_be_pc = 1325.50
sophomore_nri_be_fr = 19883

junior_r_be_pc = 573
junior_r_be_fr = 8595
junior_nri_be_pc = 1385.75
junior_nri_be_fr = 20786

senior_r_be_pc = 573
senior_r_be_fr = 8595
senior_nri_be_pc = 1385.75
senior_nri_be_fr = 20786

sf_b_js_pt = 113
sf_b_js_ft = 226

sf_e_a_pt = 402
sf_e_a_ft = 670

sf_h_js_pt = 50
sf_h_js_ft = 100

sf_s_js_pt = 50
sf_s_js_ft = 100

sf_csme_js_pt = 402
sf_csme_js_ft = 670

sf_i_pt = 375
sf_i_ft = 750

asmu_tax = 21
fm_radio_tax = 3
state_news_tax = 5
jmc_tax = 7.50

######################################################
#################### Startup text ####################
######################################################

print("2019 MSU Undergraduate Tuition Calculator.")
print()

# While loop to restart the program is the user wishes to
while restart.lower() == "yes":

    tuition = 0

    # Determine student's residential status
    resident = input("Resident (yes/no): ")
    if resident.lower() != "yes":
        international = input("International (yes/no): ")
        resident = "no"

    # While loop to re-prompt student to enter level if invalid input is entered
    while not_valid_level:

        level = input("Enter Level as freshman, sophomore, junior, senior: ")

        if level.lower() == "freshman" or level.lower() == "sophomore" or level.lower() == "junior" \
        or level.lower() == "senior":
            break
        else:
            print("Invalid input. Try again.")
            not_valid_level = True

    # If level is junior or senior, ask for college
    if level.lower() == "junior" or level.lower() == "senior":
        college = input("Enter college as business, engineering, health, sciences, or none: ")

        # Set college to none of no specified college is entered
        if not(college.lower() == "business" or college.lower() == "engineering" or college.lower() == "health" \
                or college.lower() == "sciences"):
            college = None

        # Ask if major is CMSE
        major_CMSE = input("Is your major CMSE (\"Computational Mathematics and Engineering\") (yes/no): ")

        if major_CMSE.lower() == "yes":

            # Ask if in James Madison College if major is CSME
            in_james_madison = input("Are you in the James Madison College (yes/no): ")

            if in_james_madison.lower() != "yes":
                in_james_madison = "no"

        if major_CMSE.lower() != "yes":
            major_CMSE = "no"

    # If not junior or senior, student must be freshman or sophomore
    else:
        admitted_college_engineering = input("Are you admitted to the College of Engineering (yes/no): ")
        if admitted_college_engineering.lower() != "yes":
            admitted_college_engineering = "no"

        if admitted_college_engineering.lower() != "yes":
            in_james_madison = input("Are you in the James Madison College (yes/no): ")
            if in_james_madison.lower() != "yes":
                in_james_madison = "no"

    student_credits = input("Credits: ")

    # While loop to check validity of value entered for credits
    while not_valid_credits:

        if str.isdigit(student_credits.lower()) == False or int(student_credits) <= 0:
            not_valid_credits = True
            print("Invalid input. Try again.")
            student_credits = input("Credits: ")
        else:
            not_valid_credits = False

    ##################################################
    ################## Computations ##################
    ##################################################

    ##################################################
    #################### Resident ####################
    ##################################################
    if resident.lower() == "yes":

        if int(student_credits) > 18:

            ###########################################################################################
            ############################ Tax for resident, over 6 credits  ############################
            ###########################################################################################

            tuition += asmu_tax + fm_radio_tax + state_news_tax

            if level.lower() == "freshman":

                if admitted_college_engineering.lower() == "yes":

                    # Tuition for resident, credits over 18, freshman, admitted to college of engineering
                    tuition += freshman_r_be_fr + (int(student_credits) - 18)*freshman_r_be_pc + sf_e_a_ft

                 # Not admitted to college of engineering
                elif in_james_madison == "yes":

                    # Tuition for resident, credits over 18, freshman, in james madison college
                    tuition += freshman_r_fr + (int(student_credits) - 18)*freshman_r_pc  + jmc_tax

                # Not admitted to college of engineering and not in James Madison college
                else:

                    # Tuition for resident, credits over 18, freshman, not in any college
                    tuition += freshman_r_fr + (int(student_credits) - 18)*freshman_r_pc


            elif level.lower() == "sophomore":

                if admitted_college_engineering.lower() == "yes":

                    # Tuition for resident, credits over 18, sophomore, admitted to college of engineering
                    tuition += sophomore_r_be_fr + (int(student_credits) - 18) * sophomore_r_be_pc + sf_e_a_ft

                # Not admitted to college of engineering
                elif in_james_madison == "yes":

                    # Tuition for resident, credits over 18, sophomore, in james madison college
                    tuition += sophomore_r_fr + (int(student_credits) - 18) * sophomore_r_pc + jmc_tax

                    # Not admitted to college of engineering and not in James Madison college
                else:

                    # Tuition for resident, credits over 18, sophomore, not in any college
                    tuition += sophomore_r_fr + (int(student_credits) - 18) * sophomore_r_pc

            elif level.lower() == "junior":

                if in_james_madison == "yes":
                    tuition += jmc_tax

                if major_CMSE == "yes":

                    # Add special fee - CSME is that is students major
                    tuition += sf_csme_js_ft

                if college == "business":

                    # Tuition for resident, credits over 18, junior, business college
                    tuition += junior_r_be_fr + (int(student_credits) - 18) * junior_r_be_pc + sf_b_js_ft

                elif college == "engineering":

                    # Tuition for resident, credits over 18, junior, engineering college
                    tuition += junior_r_be_fr + (int(student_credits) - 18) * junior_r_be_pc + sf_e_a_ft

                elif college == "health":

                    # Tuition for resident, credits over 18, junior, health college
                    tuition += junior_r_fr + (int(student_credits) - 18) * junior_r_pc + sf_h_js_ft

                elif college =="sciences":

                    # Tuition for resident, credits over 18, junior, sciences college
                    tuition += junior_r_fr + (int(student_credits) - 18) * junior_r_pc + sf_s_js_ft

                else:

                    # Tuition for resident, credits over 18, junior, no college
                    tuition += junior_r_fr + (int(student_credits) - 18) * junior_r_pc

            # If level not freshman, sophomore or junior then student must me senior
            else:

                if in_james_madison == "yes":
                    tuition += jmc_tax

                if major_CMSE == "yes":
                    # Add special fee - CSME is that is students major
                    tuition += sf_csme_js_ft

                if college == "business":

                    # Tuition for resident, credits over 18, senior, business college
                    tuition += senior_r_be_fr + (int(student_credits) - 18) * senior_r_be_pc + sf_b_js_ft

                elif college == "engineering":

                    # Tuition for resident, credits over 18, senior, engineering college
                    tuition += senior_r_be_fr + (int(student_credits) - 18) * senior_r_be_pc + sf_e_a_ft

                elif college == "health":

                    # Tuition for resident, credits over 18, senior, health college
                    tuition += senior_r_fr + (int(student_credits) - 18) * senior_r_pc + sf_h_js_ft

                elif college == "sciences":

                    # Tuition for resident, credits over 18, senior, sciences college
                    tuition += senior_r_fr + (int(student_credits) - 18) * senior_r_pc + sf_s_js_ft

                else:

                    # Tuition for resident, credits over 18, senior, no college
                    tuition += senior_r_fr + (int(student_credits) - 18) * senior_r_pc

        #######################################################################################
        #################### Credits in full time flat rate range resident ####################
        #######################################################################################

        elif 12 <= int(student_credits) <= 18:

            #########################################################################################
            ########################### Tax for resident, over 6 credits  ###########################
            #########################################################################################

            tuition += asmu_tax + fm_radio_tax + state_news_tax

            if level.lower() == "freshman":

                if admitted_college_engineering.lower() == "yes":

                    # Tuition for resident, credits in full time range, freshman, admitted to college of engineering
                    tuition += freshman_r_be_fr + sf_e_a_ft

                # Not admitted to college of engineering
                elif in_james_madison == "yes":

                    # Tuition for resident, credits in full time range, freshman, in james madison college
                    tuition += freshman_r_fr + jmc_tax

                # Not admitted to college of engineering and not in James Madison college
                else:

                    # Tuition for resident, credits in full time range, freshman, not in any college
                    tuition += freshman_r_fr


            elif level.lower() == "sophomore":

                if admitted_college_engineering.lower() == "yes":

                    # Tuition for resident, credits in full time range, sophomore, admitted to college of engineering
                    tuition += sophomore_r_be_fr + sf_e_a_ft

                # Not admitted to college of engineering
                elif in_james_madison == "yes":

                    # Tuition for resident, credits in full time range, sophomore, in james madison college
                    tuition += sophomore_r_fr + jmc_tax

                    # Not admitted to college of engineering and not in James Madison college
                else:

                    # Tuition for resident, credits in full time range, sophomore, not in any college
                    tuition += sophomore_r_fr

            elif level.lower() == "junior":

                if in_james_madison == "yes":
                    tuition += jmc_tax

                if major_CMSE == "yes":
                    # Add special fee - CSME is that is students major
                    tuition += sf_csme_js_ft

                if college == "business":

                    # Tuition for resident, credits in full time range, junior, business college
                    tuition += junior_r_be_fr + sf_b_js_ft

                elif college == "engineering":

                    # Tuition for resident, credits in full time range, junior, engineering college
                    tuition += junior_r_be_fr + sf_e_a_ft

                elif college == "health":

                    # Tuition for resident, credits in full time range, junior, health college
                    tuition += junior_r_fr + sf_h_js_ft

                elif college == "sciences":

                    # Tuition for resident, credits in full time range, junior, sciences college
                    tuition += junior_r_fr + sf_s_js_ft

                else:

                    # Tuition for resident, credits in full time range, junior, no college
                    tuition += junior_r_fr

            # If level not freshman, sophomore or junior then student must me senior
            else:

                if in_james_madison == "yes":
                    tuition += jmc_tax

                if major_CMSE == "yes":
                    # Add special fee - CSME is that is students major
                    tuition += sf_csme_js_ft

                if college == "business":

                    # Tuition for resident, credits in full time range, senior, business college
                    tuition += senior_r_be_fr + sf_b_js_ft

                elif college == "engineering":

                    # Tuition for resident, credits in full time range, senior, engineering college
                    tuition += senior_r_be_fr + sf_e_a_ft

                elif college == "health":

                    # Tuition for resident, credits in full time range, senior, health college
                    tuition += senior_r_fr + sf_h_js_ft

                elif college == "sciences":

                    # Tuition for resident, credits in full time range, senior, sciences college
                    tuition += senior_r_fr + sf_s_js_ft

                else:

                    # Tuition for resident, credits in full time range, senior, no college
                    tuition += senior_r_fr

        ######################################################################################################################
        #################### Credits must at this point are less that 12 so student is part-time resident ####################
        ######################################################################################################################
        else:
            ##############################################################################
            #################### Tax for resident, part-time students ####################
            ##############################################################################

            if int(student_credits) < 6:
                tuition += asmu_tax + fm_radio_tax
            else:
                tuition += asmu_tax + fm_radio_tax + state_news_tax

            if level.lower() == "freshman":

                if admitted_college_engineering.lower() == "yes":

                    # Tuition for resident, credits under 6, freshman, admitted to college of engineering
                    if int(student_credits) <= 4:
                        tuition += (int(student_credits)) * freshman_r_be_pc + sf_e_a_pt
                    else:
                        tuition += (int(student_credits)) * freshman_r_be_pc + sf_e_a_ft

                 # Not admitted to college of engineering
                elif in_james_madison == "yes":

                    # Tuition for resident, credits under 6, freshman, in james madison college
                    tuition += (int(student_credits))*freshman_r_pc  + jmc_tax

                # Not admitted to college of engineering and not in James Madison college
                else:

                    # Tuition for resident, credits under 6, freshman, not in any college
                    tuition += (int(student_credits))*freshman_r_pc


            elif level.lower() == "sophomore":

                if admitted_college_engineering.lower() == "yes":

                    # Tuition for resident, credits under 6, sophomore, admitted to college of engineering
                    if int(student_credits) <= 4:
                        tuition += (int(student_credits)) * sophomore_r_be_pc + sf_e_a_pt
                    else:
                        tuition += (int(student_credits)) * sophomore_r_be_pc + sf_e_a_ft

                # Not admitted to college of engineering
                elif in_james_madison == "yes":

                    # Tuition for resident, credits under 6, sophomore, in james madison college
                    tuition += (int(student_credits)) * sophomore_r_pc + jmc_tax

                    # Not admitted to college of engineering and not in James Madison college
                else:

                    # Tuition for resident, credits under 6, sophomore, not in any college
                    tuition += (int(student_credits)) * sophomore_r_pc

            elif level.lower() == "junior":

                if in_james_madison == "yes":
                    tuition += jmc_tax

                if major_CMSE == "yes":
                     # Add special fee - CSME is that is students major
                    if int(student_credits) <= 4:
                        tuition += sf_csme_js_pt
                    else:
                        tuition += sf_csme_js_ft

                if college == "business":

                    # Tuition for resident, credits under 6, junior, business college
                    if int(student_credits) <= 4:
                        tuition += (int(student_credits)) * junior_r_be_pc + sf_b_js_pt
                    else:
                        tuition += (int(student_credits)) * junior_r_be_pc + sf_b_js_ft

                elif college == "engineering":

                    # Tuition for resident, credits under 6, junior, engineering college
                    if int(student_credits) <= 4:
                        tuition += (int(student_credits)) * junior_r_be_pc + sf_e_a_pt
                    else:
                        tuition += (int(student_credits)) * junior_r_be_pc + sf_e_a_ft

                elif college == "health":

                    # Tuition for resident, credits under 6, junior, health college
                    if int(student_credits) <= 4:
                        tuition += (int(student_credits)) * junior_r_pc + sf_h_js_pt
                    else:
                        tuition += (int(student_credits)) * junior_r_pc + sf_h_js_ft

                elif college =="sciences":

                    # Tuition for resident, credits under 6, junior, sciences college
                    if int(student_credits) <= 4:
                        tuition += (int(student_credits)) * junior_r_pc + sf_s_js_pt
                    else:
                        tuition += (int(student_credits)) * junior_r_pc + sf_s_js_ft

                else:

                    # Tuition for resident, credits under 6, junior, no college
                    tuition += (int(student_credits)) * junior_r_pc

            # If level not freshman, sophomore or junior then student must me senior #
            else:

                if in_james_madison == "yes":
                    tuition += jmc_tax

                if major_CMSE == "yes":
                    # Add special fee - CSME is that is students major
                    if int(student_credits) <= 4:
                        tuition += sf_csme_js_pt
                    else:
                        tuition += sf_csme_js_ft

                if college == "business":

                    # Tuition for resident, credits under 6, senior, business college
                    if int(student_credits) <= 4:
                        tuition += (int(student_credits)) * senior_r_be_pc + sf_b_js_pt
                    else:
                        tuition += (int(student_credits)) * senior_r_be_pc + sf_b_js_ft

                elif college == "engineering":

                    # Tuition for resident, credits under 6, senior, engineering college
                    if int(student_credits) <= 4:
                        tuition += (int(student_credits)) * senior_r_be_pc + sf_e_a_pt
                    else:
                        tuition += (int(student_credits)) * senior_r_be_pc + sf_e_a_ft

                elif college == "health":

                    # Tuition for resident, credits under 6, senior, health college
                    if int(student_credits) <= 4:
                        tuition += (int(student_credits)) * senior_r_pc + sf_h_js_pt
                    else:
                        tuition += (int(student_credits)) * senior_r_pc + sf_h_js_ft

                elif college == "sciences":

                    # Tuition for resident, credits under 6, senior, sciences college
                    if int(student_credits) <= 4:
                        tuition += (int(student_credits)) * senior_r_pc + sf_s_js_pt
                    else:
                        tuition += (int(student_credits)) * senior_r_pc + sf_s_js_ft

                else:

                    # Tuition for resident, credits under 6, senior, no college
                    tuition += senior_r_fr + (int(student_credits)) * senior_r_pc

    ##################################################################################################
    ############### if not resident then student must be non-resident or international ###############
    ##################################################################################################

    elif resident.lower() == "no":

        if international == "yes":

            ###################################################################################################
            ################### Add special fee - international if student is international ###################
            ###################################################################################################

            tuition += sf_i_ft

        if int(student_credits) > 18:

            ############################################################################################
            #################### Tax for non-resident/international, over 6 credits ####################
            ############################################################################################

            tuition += asmu_tax + fm_radio_tax + state_news_tax

            if level.lower() == "freshman":

                if admitted_college_engineering.lower() == "yes":

                    # Tuition for nri, credits over 18, freshman, admitted to college of engineering
                    tuition += freshman_nri_be_fr + (int(student_credits) - 18)*freshman_nri_be_pc + sf_e_a_ft

                elif in_james_madison == "yes":

                    # Tuition for nri, credits over 18, freshman, in james madison college
                    tuition += freshman_nri_fr + (int(student_credits) - 18)*freshman_nri_pc + jmc_tax

                else:

                    # Tuition for nri, credits over 18, freshman, not in any college
                    tuition += freshman_nri_fr + (int(student_credits)- 18) * freshman_nri_pc

            elif level.lower() == "sophomore":

                if admitted_college_engineering.lower() == "yes":

                    # Tuition for nri, credits over 18, sophomore, admitted to college of engineering
                    tuition += sophomore_nri_be_fr + (int(student_credits) - 18) * sophomore_nri_be_pc + sf_e_a_ft

                elif in_james_madison == "yes":

                    # Tuition for nri, credits over 18, sophomore, in james madison college
                    tuition += sophomore_nri_fr + (int(student_credits) - 18) * sophomore_nri_pc + jmc_tax

                else:

                    # Tuition for nri, credits over 18, sophomore, not in any college
                    tuition += sophomore_nri_fr + (int(student_credits) - 18) * sophomore_nri_pc

            elif level.lower() == "junior":

                if in_james_madison == "yes":
                    tuition += jmc_tax

                if major_CMSE == "yes":

                    # Add special fee - CSME is that is students major
                    tuition += sf_csme_js_ft

                if college == "business":

                    # Tuition for nri, credits over 18, junior, business college
                    tuition += junior_nri_be_fr + (int(student_credits) - 18) * junior_nri_be_pc + sf_b_js_ft

                elif college == "engineering":

                    # Tuition for nri, credits over 18, junior, engineering college
                    tuition += junior_nri_be_fr + (int(student_credits) - 18) * junior_nri_be_pc + sf_e_a_ft

                elif college == "health":

                    # Tuition for nri, credits over 18, junior, health college
                    tuition += junior_nri_fr + (int(student_credits) - 18) * junior_nri_pc + sf_h_js_ft

                elif college =="sciences":

                    # Tuition for nri, credits over 18, junior, sciences college
                    tuition += junior_nri_fr + (int(student_credits) - 18) * junior_nri_pc + sf_s_js_ft

                else:

                    # Tuition for nri, credits over 18, junior, no college
                    tuition += junior_nri_fr + (int(student_credits) - 18) * junior_nri_pc

            # If level not freshman, sophomore or junior then student must me senior
            else:

                if in_james_madison == "yes":
                    tuition += jmc_tax

                if major_CMSE == "yes":

                    # Add special fee - CSME is that is students major
                    tuition += sf_csme_js_ft

                if college == "business":

                    # Tuition for nri, credits over 18, senior, business college
                    tuition += senior_nri_be_fr + (int(student_credits) - 18) * senior_nri_be_pc + sf_b_js_ft

                elif college == "engineering":

                    # Tuition for nri, credits over 18, senior, engineering college
                    tuition += senior_nri_be_fr + (int(student_credits) - 18) * senior_nri_be_pc + sf_e_a_ft

                elif college == "health":

                    # Tuition for nri, credits over 18, senior, health college
                    tuition += senior_nri_fr + (int(student_credits) - 18) * senior_nri_pc + sf_h_js_ft

                elif college =="sciences":

                    # Tuition for nri, credits over 18, senior, sciences college
                    tuition += senior_nri_fr + (int(student_credits) - 18) * senior_nri_pc + sf_s_js_ft

                else:

                    # Tuition for nri, credits over 18, senior, no college
                    tuition += senior_nri_fr + (int(student_credits) - 18) * senior_nri_pc

        #########################################################################################################
        #################### credits in full time flat rate range non-resident/international ####################
        #########################################################################################################

        elif 12 <= int(student_credits) <= 18:

            ############################################################################################
            #################### Tax for non-resident/international, credits over 6 ####################
            ############################################################################################

            tuition += asmu_tax + fm_radio_tax + state_news_tax

            if level.lower() == "freshman":

                if admitted_college_engineering.lower() == "yes":

                    # Tuition for nri, credits in full time range, freshman, admitted to college of engineering
                    tuition += freshman_nri_be_fr + sf_e_a_ft

                # Not admitted to college of engineering
                elif in_james_madison == "yes":

                    # Tuition for nri, credits in full time range, freshman, in james madison college
                    tuition += freshman_nri_fr + jmc_tax

                # Not admitted to college of engineering and not in James Madison college
                else:

                    # Tuition for nri, credits in full time range, freshman, not in any college
                    tuition += freshman_nri_fr


            elif level.lower() == "sophomore":

                if admitted_college_engineering.lower() == "yes":

                    # Tuition for nri, credits in full time range, sophomore, admitted to college of engineering
                    tuition += sophomore_nri_be_fr + sf_e_a_ft

                # Not admitted to college of engineering
                elif in_james_madison == "yes":

                    # Tuition for nri, credits in full time range, sophomore, in james madison college
                    tuition += sophomore_nri_fr + jmc_tax

                    # Not admitted to college of engineering and not in James Madison college
                else:

                    # Tuition for nri, credits in full time range, sophomore, not in any college
                    tuition += sophomore_nri_fr

            elif level.lower() == "junior":

                if in_james_madison == "yes":
                    tuition += jmc_tax

                if major_CMSE == "yes":
                    # Add special fee - CSME is that is students major
                    tuition += sf_csme_js_ft

                if college == "business":

                    # Tuition for nri, credits in full time range, junior, business college
                    tuition += junior_nri_be_fr + sf_b_js_ft

                elif college == "engineering":

                    # Tuition for nri, credits in full time range, junior, engineering college
                    tuition += junior_nri_be_fr + sf_e_a_ft

                elif college == "health":

                    # Tuition for nri, credits in full time range, junior, health college
                    tuition += junior_nri_fr + sf_h_js_ft

                elif college == "sciences":

                    # Tuition for nri, credits in full time range, junior, sciences college
                    tuition += junior_nri_fr + sf_s_js_ft

                else:

                    # Tuition for nri, credits in full time range, junior, no college
                    tuition += junior_nri_fr

            # If level not freshman, sophomore or junior then student must me senior
            else:

                if in_james_madison == "yes":
                    tuition += jmc_tax

                if major_CMSE == "yes":
                    # Add special fee - CSME is that is students major
                    tuition += sf_csme_js_ft

                if college == "business":

                    # Tuition for nri, credits in full time range, senior, business college
                    tuition += senior_nri_be_fr + sf_b_js_ft

                elif college == "engineering":

                    # Tuition for nri, credits in full time range, senior, engineering college
                    tuition += senior_nri_be_fr + sf_e_a_ft

                elif college == "health":

                    # Tuition for nri, credits in full time range, senior, health college
                    tuition += senior_nri_fr + sf_h_js_ft

                elif college == "sciences":

                    # Tuition for nri, credits in full time range, senior, sciences college
                    tuition += senior_nri_fr + sf_s_js_ft

                else:

                    # Tuition for nri, credits in full time range, senior, no college
                    tuition += senior_nri_fr

        ######################################################################################################################
        ########### Credits must at this point are less that 12 so student is part-time non-resident/international ###########
        ######################################################################################################################

        else:

            ################################################################################################
            #################### Tax for non-resident/international, part-time students ####################
            ################################################################################################

            if int(student_credits) < 6:
                tuition += asmu_tax + fm_radio_tax
            else:
                tuition += asmu_tax + fm_radio_tax + state_news_tax

            if level.lower() == "freshman":

                if admitted_college_engineering.lower() == "yes":

                    # Tuition for nri, credits under 6, freshman, admitted to college of engineering
                    if int(student_credits) <= 4:
                        tuition += (int(student_credits)) * freshman_nri_be_pc + sf_e_a_pt
                    else:
                        tuition += (int(student_credits)) * freshman_nri_be_pc + sf_e_a_ft

                # Not admitted to college of engineering
                elif in_james_madison == "yes":

                    # Tuition for nri, credits under 6, freshman, in james madison college
                    tuition += (int(student_credits)) * freshman_nri_pc + jmc_tax

                # Not admitted to college of engineering and not in James Madison college
                else:

                    # Tuition for nri, credits under 6, freshman, not in any college
                    tuition += (int(student_credits)) * freshman_nri_pc


            elif level.lower() == "sophomore":

                if admitted_college_engineering.lower() == "yes":

                    # Tuition for nri, credits under 6, sophomore, admitted to college of engineering
                    if int(student_credits) <= 4:
                        tuition += (int(student_credits)) * sophomore_nri_be_pc + sf_e_a_pt
                    else:
                        tuition += (int(student_credits)) * sophomore_nri_be_pc + sf_e_a_ft

                # Not admitted to college of engineering
                elif in_james_madison == "yes":

                    # Tuition for nri, credits under 6, sophomore, in james madison college
                    tuition += (int(student_credits)) * sophomore_nri_pc + jmc_tax

                    # Not admitted to college of engineering and not in James Madison college
                else:

                    # Tuition for nri, credits under 6, sophomore, not in any college
                    tuition += (int(student_credits)) * sophomore_nri_pc

            elif level.lower() == "junior":

                if in_james_madison == "yes":
                    tuition += jmc_tax

                if major_CMSE == "yes":
                    # Add special fee - CSME is that is students major
                    if int(student_credits) <= 4:
                        tuition += sf_csme_js_pt
                    else:
                        tuition += sf_csme_js_ft

                if college == "business":

                    # Tuition for nri, credits under 6, junior, business college
                    if int(student_credits) <= 4:
                        tuition += (int(student_credits)) * junior_nri_be_pc + sf_b_js_pt
                    else:
                        tuition += (int(student_credits)) * junior_nri_be_pc + sf_b_js_ft

                elif college == "engineering":

                    # Tuition for nri, credits under 6, junior, engineering college
                    if int(student_credits) <= 4:
                        tuition += (int(student_credits)) * junior_nri_be_pc + sf_e_a_pt
                    else:
                        tuition += (int(student_credits)) * junior_nri_be_pc + sf_e_a_ft

                elif college == "health":

                    # Tuition for nri, credits under 6, junior, health college
                    if int(student_credits) <= 4:
                        tuition += (int(student_credits)) * junior_nri_pc + sf_h_js_pt
                    else:
                        tuition += (int(student_credits)) * junior_nri_pc + sf_h_js_ft

                elif college == "sciences":

                    # Tuition for nri, credits under 6, junior, sciences college
                    if int(student_credits) <= 4:
                        tuition += (int(student_credits)) * junior_nri_pc + sf_s_js_pt
                    else:
                        tuition += (int(student_credits)) * junior_nri_pc + sf_s_js_ft
                else:

                    # Tuition for nri, credits under 6, junior, no college
                    tuition += (int(student_credits)) * junior_nri_pc

            # If level not freshman, sophomore or junior then student must me senior
            else:

                if in_james_madison == "yes":
                    tuition += jmc_tax

                if major_CMSE == "yes":
                    # Add special fee - CSME is that is students major
                    if int(student_credits) <= 4:
                        tuition += sf_csme_js_pt
                    else:
                        tuition += sf_csme_js_ft

                if college == "business":

                    # Tuition for nri, credits under 6, senior, business college
                    if int(student_credits) <= 4:
                        tuition += (int(student_credits)) * senior_nri_be_pc + sf_b_js_pt
                    else:
                        tuition += (int(student_credits)) * senior_nri_be_pc + sf_b_js_ft

                elif college == "engineering":

                    # Tuition for nri, credits under 6, senior, engineering college
                    if int(student_credits) <= 4:
                        tuition += (int(student_credits)) * senior_nri_be_pc + sf_e_a_pt
                    else:
                        tuition += (int(student_credits)) * senior_nri_be_pc + sf_e_a_ft

                elif college == "health":

                    # Tuition for nri, credits under 6, senior, health college
                    if int(student_credits) <= 4:
                        tuition += (int(student_credits)) * senior_nri_pc + sf_h_js_pt
                    else:
                        tuition += (int(student_credits)) * senior_nri_pc + sf_h_js_ft

                elif college == "sciences":

                    # Tuition for nri, credits under 6, senior, sciences college
                    if int(student_credits) <= 4:
                        tuition += (int(student_credits)) * senior_nri_pc + sf_s_js_pt
                    else:
                        tuition += (int(student_credits)) * senior_nri_pc + sf_s_js_ft

                else:

                    # Tuition for nri, credits under 6, senior, no college
                    tuition += senior_nri_fr + (int(student_credits) - 18) * senior_nri_pc

    tuition = float(tuition)
    formatted_tuition = "${:,.2f}".format(tuition)
    print("Tuition is" + " " + formatted_tuition + ".")
    restart = input("Do you want to do another calculation (yes/no): ")


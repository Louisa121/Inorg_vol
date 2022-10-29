def vol_inorg(ams):
    ##### ams is Dataframe with columns NH4, SO4, NO3, and Chl ####
    # density
    Rho_NH4NO3 = 1.72                                       # From lide, 2001, Fierz et al., 2010
    Rho_NH42SO4 = 1.77                                      # From Lide, 2001, Fierz et al., 2010
    Rho_Na2SO4 = 2.66                                      # Wiki
    Rho_NH4HSO4 = 1.78                                      # From Fierz et al., 2010
    Rho_NH4Cl = 1.53
    
    n = ams.NH4/18
    s = ams.SO4/96
    n_mNO3 = n - ams.NO3/62 - ams.Chl/35.5
    n_NH4NO3 = np.zeros(len(n))
    n_NH42SO4 = np.zeros(len(n))
    n_NH4HSO4 = np.zeros(len(n))
    n_NH4Cl = np.zeros(len(n))
    n_residual_N = np.zeros(len(n))
    n_residual_S = np.zeros(len(n))
    for i in range(len(n)):
        if n_mNO3[i] - 2*s[i]>0:
            n_NH4NO3[i] = ams.NO3[i]/62  
            n_NH4Cl[i] = ams.Chl[i]/35.5
            n_NH42SO4[i] = s[i]
            n_residual_N[i] = n_mNO3[i] - 2*s[i]
    #                 print('2')
        elif n_mNO3[i]-s[i]>0:
            n_NH4NO3[i] = ams.NO3[i]/62
            n_NH4Cl[i] = ams.Chl[i]/35.5
            n_NH42SO4[i] = n_mNO3[i] - s[i] 
            n_NH4HSO4[i] = 2*s[i] - n_mNO3[i] 
    #                 n_residual_N[i] = n_mNO3[i] - 2*n_NH42SO4[i] - n_NH4HSO4[i]
    #                 print('3')
        elif n_mNO3[i]>0:
            n_NH4NO3[i] = ams.NO3[i]/62
            n_NH4Cl[i] = ams.Chl[i]/35.5
            n_NH4HSO4[i] = n_mNO3[i]
            n_residual_S[i] = s[i] - n_mNO3[i]
        else:
            n_NH4NO3[i] = ams.NH4[i]/18
            n_NH4Cl[i] = ams.Chl[i]/35.5

    v_NH42SO4 = (n_NH42SO4*132)/Rho_NH42SO4
    v_Na2SO4 = (n_residual_S*142)/Rho_Na2SO4
    v_NH4NO3 = (n_NH4NO3*80)/Rho_NH4NO3
    v_NH4HSO4 = (n_NH4HSO4*115)/Rho_NH4HSO4
    v_NH4Cl = n_NH4Cl*53.5/Rho_NH4Cl
       
    return(v_NH42SO4,v_Na2SO4,v_NH4NO3,v_NH4HSO4,v_NH4Cl)

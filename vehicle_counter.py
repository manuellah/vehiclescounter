class vehicles(object):
    def populate_no_plates():
        '''
        Number plate syntax LLL NNNL, Where L=Letter and N=Nummber eg KBA 012Z
        
        My assumptions:
            0. The first latter K is always a constant.
            1. In a constant number plate with variable last latter there are 26 vehicles 
                 produced, ie from KAA 001A to KAA 001Z 26 cars where bought
            2. To change the third latter to the other, a single letter holds 25974(999 * 26) cars,
                  ie, From KAA 001A to KAA 999Z(KAA 001A - KAB 001A)
            3. I also figured out that for the second variable to change, a total of 675324(999 * 26 * 26) cars
                  where produced, ie, From KAA 001A to KAZ 999Z(KAA 001A - KBA 001A)
            4. No special Number Plates, Every Number is given to each car bought 
        
        This particular method populate the dictionary whose key are the A-Z with each key holding a tuple 
        with three elements:
            (a) First element maps the last latter of the Number plate with its corresponding number between 1-26
            (b) Second element maps the third latter of the number plate and represents the vehicles bought prior that              particular series eg To get to KAC, 51948(2 * 999 * 26) vehicles where bought ie for KAA and KAB
            (c) Third element maps the second latter of the number plate and represents the vehicles bought prior that              particular series eg To get to KDA, 2025972(3 * 999 * 26 * 26) vehicles where bought ie for KAA , KBA and KCA
            
        '''
        no_plates = {}
        num = 0
        while i = 65:
            no_plates[chr(i)] = (num + 1, num * 999 * 26, num  * 999 * 26 )
        
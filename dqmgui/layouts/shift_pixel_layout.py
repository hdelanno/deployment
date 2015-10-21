def shiftpixellayout(i, p, *rows): i["00 Shift/Pixel/" + p] = DQMItem(layout=rows)
shiftpixellayout(dqmitems, "00 - Pixel Summary Map",
  [{ 'path': "Pixel/EventInfo/reportSummaryMap",
     'description': "Pixel Report Summary Map: FED data vs. lumisections",
     'draw': { 'withref': "no" }}]
  )
shiftpixellayout(dqmitems, "01 - Total number of errors",
  [{ 'path': "Pixel/AdditionalPixelErrors/FedChNErr",
     'description': "Total number of errors in a map of FED channels (y-axis) vs. FED (x-axis). Look for channels with thousands of errors!",
     'draw': { 'withref': "no" }}]
  )
shiftpixellayout(dqmitems, "02 - Error types",
  [{ 'path': "Pixel/AdditionalPixelErrors/FedETypeNErr",
     'description': "Total number of errors per error type (y-axis) vs. FED (x-axis). Large amounts (hundreds)of errors other than Timeout, EventNumber, and Dcol,Pixel values would be unusual!",
     'draw': { 'withref': "no" }}]
  )
shiftpixellayout(dqmitems, "03 - Cluster occupancy Barrel Layer 1",
  [{ 'path': "Pixel/Clusters/OffTrack/position_siPixelClusters_Layer_1",
     'description': "Cluster occupancy of Barrel Layer 1. Look for new holes compared to the example plot.",
     'draw': { 'withref': "no" }}]
  )
shiftpixellayout(dqmitems, "04 - Cluster occupancy Barrel Layer 2",
  [{ 'path': "Pixel/Clusters/OffTrack/position_siPixelClusters_Layer_2",
     'description': "Cluster occupancy of Barrel Layer 2. Look for new holes compared to the example plot.",
     'draw': { 'withref': "no" }}]
  )
shiftpixellayout(dqmitems, "05 - Cluster occupancy Barrel Layer 3",
  [{ 'path': "Pixel/Clusters/OffTrack/position_siPixelClusters_Layer_3",
     'description': "Cluster occupancy of Barrel Layer 3. Look for new holes compared to the example plot.",
     'draw': { 'withref': "no" }}]
  )
shiftpixellayout(dqmitems, "06 - Cluster occupancy Endcap -z Disk 1",
  [{ 'path': "Pixel/Clusters/OffTrack/position_siPixelClusters_mz_Disk_1",
     'description': "Cluster occupancy of Endcap -z Disk 1. Look for new holes compared to the example plot.",
     'draw': { 'withref': "no" }}]
  )
shiftpixellayout(dqmitems, "07 - Cluster occupancy Endcap -z Disk 2",
  [{ 'path': "Pixel/Clusters/OffTrack/position_siPixelClusters_mz_Disk_2",
     'description': "Cluster occupancy of Endcap -z Disk 2. Look for new holes compared to the example plot.",
     'draw': { 'withref': "no" }}]
  )
shiftpixellayout(dqmitems, "08 - Cluster occupancy Endcap +z Disk 1",
  [{ 'path': "Pixel/Clusters/OffTrack/position_siPixelClusters_pz_Disk_1",
     'description': "Cluster occupancy of Endcap +z Disk 1. Look for new holes compared to the example plot.",
     'draw': { 'withref': "no" }}]
  )
shiftpixellayout(dqmitems, "09 - Cluster occupancy Endcap +z Disk 2",
  [{ 'path': "Pixel/Clusters/OffTrack/position_siPixelClusters_pz_Disk_2",
     'description': "Cluster occupancy of Endcap +z Disk 2. Look for new holes compared to the example plot.",
     'draw': { 'withref': "no" }}]
  )
shiftpixellayout(dqmitems, "10 - Barrel cluster charge",
  [{ 'path': "Pixel/Barrel/SUMCLU_charge_Barrel",
     'description': "Mean cluster charge in kilo electrons per Barrel module",
     'draw': { 'withref': "no" }}]
  )
shiftpixellayout(dqmitems, "11 - Barrel cluster size",
  [{ 'path': "Pixel/Barrel/SUMCLU_size_Barrel",
     'description': "Mean cluster size in number of pixels per Barrel module",
     'draw': { 'withref': "no" }}]
  )
shiftpixellayout(dqmitems, "12 - Endcap cluster charge",
  [{ 'path': "Pixel/Endcap/SUMCLU_charge_Endcap",
     'description': "Mean cluster charge in kilo electrons per Endcap module",
     'draw': { 'withref': "no" }}]
  )
shiftpixellayout(dqmitems, "13 - Endcap cluster size",
  [{ 'path': "Pixel/Endcap/SUMCLU_size_Endcap",
     'description': "Mean cluster size in number of pixels per Endcap module",
     'draw': { 'withref': "no" }}]
  )
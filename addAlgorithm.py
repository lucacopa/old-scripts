#!/usr/bin/env python



from ProdCommon.DataMgmt.DBS.DBSWriter import DBSWriter
from ProdCommon.DataMgmt.DBS.DBSWriterObjects import createAlgorithm






dbsUrl="https://cmst0dbs.cern.ch:8443/cms_dbs_prod_tier0_writer/servlet/DBSServlet"
procDataset = "/Cosmics/CRUZET3-v1/RAW"


writer = DBSWriter(dbsUrl)



datasetInfo = {}
datasetInfo['ApplicationName'] = "cmsRun"
datasetInfo['ApplicationVersion'] = "CMSSW_2_0_10"
datasetInfo["ApplicationFamily"] = "Merged"
datasetInfo['PSetHash'] = "PSET_HASH_NOT_AVAILABLE"
datasetInfo['PSetContent'] = "PSET CONTENT NOT AVAILABLE"


configMetadata = {}
configMetadata['name'] = "RepackerMerger-%s" % procDataset # need dataset name
configMetadata['version'] = "AutoGenerated"
configMetadata['annotation'] = "AutoGenerated By Tier 0"
configMetadata['Type'] = "data" # RequestCategory





algo = createAlgorithm(datasetInfo, configMetadata)
writer.dbs.insertAlgorithm(algo)
writer.dbs.insertAlgoInPD(procDataset, algo)
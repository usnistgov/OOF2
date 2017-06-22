// Architecture mock-up for plasticity code:


// Presumes the existence of a Material class with a begin_element
// routine....


class Material {
private:
  // ...
// Slightly unsafe, you might need element-specific pds in the pll case.
  PlasticData *pd;
  // ...
}

Material::begin_element(Element *el) {
  ElementData *ed = el->getDataByName("plastic_data");
  if (el==0) {
    pd = new PlasticData("plastic_data",...);
    el->setDataByName(pd,"plastic_data");
  }
  else {
    pd = dynamic_cast<PlasticData*>(ed);
  }
  // ...
}


Material::end_element(Element *el) {
  // Plastic computations...
  el->setDataByName(pd,"plastic_data");
}



class GptPlasticData {
public:
  std::vector<double> fp, fpt;
  GptPLasticData();
};

GptPlasticData::GptPlasticData {
  // Non-stupid constructor -- identity matrices, probably.
}
  
class PlasticData : public ElementData {
public:
  PlasticData(Element *el);
  std::vector<SmallMatrix*> fp;
};

PlasticData::PlasticData(Element *el) : ElementData("plastic_data") {
  for (GaussPointIterator gpti = el>gpt_start();
       gpti!=el->gpt_end(); gpti++) {
    GptPLasticData *gppd = GptPlasticData()
    fp.push_back(gppd);
  }
}

#include <mbgl/layer/background_layer.hpp>
#include <mbgl/renderer/bucket.hpp>

namespace mbgl {

std::unique_ptr<StyleLayer> BackgroundLayer::clone() const {
    return std::make_unique<BackgroundLayer>(*this);
}

void BackgroundLayer::parsePaints(const JSValue& layer) {
    paint.opacity.parse("background-opacity", layer);
    paint.color.parse("background-color", layer);
    paint.pattern.parse("background-pattern", layer);
}

void BackgroundLayer::cascade(const StyleCascadeParameters& parameters) {
    paint.opacity.cascade(parameters);
    paint.color.cascade(parameters);
    paint.pattern.cascade(parameters);
}

bool BackgroundLayer::recalculate(const StyleCalculationParameters& parameters) {
    bool hasTransitions = false;

    hasTransitions |= paint.opacity.calculate(parameters);
    hasTransitions |= paint.color.calculate(parameters);
    hasTransitions |= paint.pattern.calculate(parameters);

    passes = paint.opacity > 0 ? RenderPass::Translucent : RenderPass::None;

    return hasTransitions;
}

std::unique_ptr<Bucket> BackgroundLayer::createBucket(StyleBucketParameters&) const {
    return nullptr;
}

} // namespace mbgl
